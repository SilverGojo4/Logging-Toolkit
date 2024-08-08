"""
Module for configuring and setting up logging.
此模組提供設置日誌
"""

import json
import logging
import logging.config
import os


def setup_logging(
    config_file: str = "logging_config.json",
    logger_name: str = __name__,
    handler_name: str = "file",
) -> logging.Logger:
    """
    從 JSON 配置文件載入並應用日誌配置

    ## Parameters
    ----------
    - config_file: str, 日誌配置文件的路徑
    - logger_name: str, 日誌記錄器的名稱
    - handler_name: str, 處理器的名稱

    ## Returns
    ----------
    - logger: logging.Logger, 配置完成的日誌記錄器
    """
    # 設置臨時日誌配置, 包含格式化輸出
    logging.basicConfig(
        level=logging.ERROR,
        format="%(levelname)-8s: %(message)s",
    )

    # 創建一個臨時的 logger 對象, 用來記錄配置過程中的錯誤
    temp_logger = logging.getLogger("temporary_logger")

    try:
        # 嘗試打開並讀取 JSON 配置文件
        with open(config_file, "r", encoding="utf-8") as file:
            # 將 JSON 文件內容加載為字典, 這裡的 config_dict 包含了日誌的配置信息
            config_dict = json.load(file)

            # 嘗試從配置中獲取指定 handler 的日誌文件路徑
            log_path = (
                config_dict.get("handlers", {})
                .get(handler_name, {})
                .get("filename", None)
            )

            # 如果獲取到了 log_path, 需要確認該日誌文件的目錄是否存在
            if log_path:
                log_dir = os.path.dirname(log_path)

                # 如果目錄不存在, 則拋出 FileNotFoundError 錯誤
                if not os.path.exists(log_dir):
                    raise FileNotFoundError(
                        f"Logging directory does not exist: {log_dir}"
                    )

            # 如果所有步驟都成功, 則應用從 JSON 文件中讀取的日誌配置
            logging.config.dictConfig(config_dict)

            # 獲取並返回配置完成的 logger 對象
            logger = logging.getLogger(logger_name)
            return logger

    # 捕獲文件打開或讀取過程中可能發生的錯誤
    except (PermissionError, FileNotFoundError, json.JSONDecodeError) as file_error:
        # 使用臨時 logger 記錄錯誤信息, 方便調試和排查問題
        temp_logger.error("File error occurred: %s", file_error)
        raise

    # 捕獲配置過程中可能出現的錯誤
    except (ValueError, KeyError) as config_error:
        # 使用臨時 logger 記錄錯誤信息, 提示用戶配置文件中可能存在問題
        temp_logger.error("Configuration error occurred: %s", config_error)
        raise

    # 捕獲任何其他未預見的異常
    except Exception as unexpected_error:
        # 使用臨時 logger 記錄錯誤信息, 幫助識別潛在的未知問題
        temp_logger.error("Unexpected error occurred: %s", unexpected_error)
        raise
