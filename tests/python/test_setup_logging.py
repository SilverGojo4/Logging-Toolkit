"""
Tests for the setup_logging function in the Logging-Toolkit.
測試 Logging-Toolkit 中的 setup_logging 函數
"""

# Importing necessary modules and functions
import os
import sys

import pytest

sys.path.append("src/python/")  # pylint: disable=wrong-import-position
from setup_logging import setup_logging  # pylint: disable=import-error


# Define the test function for setup_logging
def test_setup_logging():
    """
    測試 setup_logging 函數的日誌記錄器配置及文件輸出是否正確
    """
    # 使用測試用的配置文件
    config_path = "src/python/logging_config.json"

    # 執行 setup_logging 函數，配置 file_logger 和 error_logger
    file_logger = setup_logging(
        config_file=config_path, logger_name="general_logger", handler_name="file"
    )
    error_logger = setup_logging(
        config_file=config_path, logger_name="error_logger", handler_name="error_file"
    )

    # 測試 file_logger 是否正確配置
    assert file_logger is not None
    file_logger.debug("This is a DEBUG message.")
    file_logger.info("This is an INFO message.")
    file_logger.warning("This is a WARNING message.")
    file_logger.error("This is an ERROR message.")
    file_logger.critical("This is a CRITICAL message.")

    # 測試 error_logger 是否正確配置
    assert error_logger is not None
    error_logger.debug("This is a DEBUG message.")
    error_logger.info("This is an INFO message.")
    error_logger.warning("This is a WARNING message.")
    error_logger.error("This is an ERROR message.")
    error_logger.critical("This is a CRITICAL message.")

    # 檢查 file_logger 的日誌文件
    file_log_path = "tests/python/file_log.log"
    assert os.path.exists(file_log_path), f"File log not found: {file_log_path}"

    # 檢查 error_logger 的日誌文件
    error_log_path = "tests/python/error_log.log"
    assert os.path.exists(error_log_path), f"Error log not found: {error_log_path}"

    # 清理日誌文件 (可選)
    if os.path.exists(file_log_path):
        os.remove(file_log_path)
    if os.path.exists(error_log_path):
        os.remove(error_log_path)


# Run the test if this script is executed as the main program
if __name__ == "__main__":
    pytest.main()
