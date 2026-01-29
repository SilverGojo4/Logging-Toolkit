# pylint: disable=
"""
Logging backend initialization utilities.

This module provides a standardized interface for configuring
Python logging using JSON-based configuration files.
"""

from __future__ import annotations

# Standard Library Imports
import json
import logging
import logging.config
import os
from typing import Optional, cast

# Package Imports
from logging_toolkit.logger import CustomLogger


def setup_logging(
    *,
    input_config_file: str,
    logger_name: str,
    handler_name: str,
    output_log_path: Optional[str] = None,
) -> CustomLogger:
    """
    Initialize and return a configured CustomLogger instance.

    Parameters
    ----------
    input_config_file : str
        Path to the logging configuration JSON file.
    logger_name : str
        Name of the logger to retrieve.
    handler_name : str
        Name of the handler whose output path may be overridden.
    output_log_path : str, optional
        Override path for the log file output.

    Returns
    -------
    CustomLogger
        Initialized logger instance.

    Raises
    ------
    FileNotFoundError
        If the logging configuration file does not exist.
    json.JSONDecodeError
        If the configuration file is not valid JSON.
    KeyError
        If the specified handler is not defined in the configuration.
    """

    # Register CustomLogger globally
    logging.setLoggerClass(CustomLogger)

    # Temporary fallback configuration
    logging.basicConfig(
        level=logging.WARNING,
        format="%(asctime)s - %(levelname)-8s -",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Load logging configuration
    with open(input_config_file, "r", encoding="utf-8") as f:
        config_dict = json.load(f)

    # Override handler output path if provided
    if output_log_path:
        handlers = config_dict.get("handlers", {})

        if handler_name not in handlers:
            raise KeyError(
                f"Handler '{handler_name}' not found in logging configuration."
            )

        handlers[handler_name]["filename"] = output_log_path

        log_dir = os.path.dirname(output_log_path)
        if log_dir:
            os.makedirs(log_dir, exist_ok=True)

    # Apply logging configuration
    logging.config.dictConfig(config_dict)

    # Retrieve configured logger
    logger = cast(CustomLogger, logging.getLogger(logger_name))
    return logger
