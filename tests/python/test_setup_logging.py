# pylint: disable=wrong-import-position, import-error, line-too-long
"""
Tests for the setup_logging function in the logging-toolkit.
"""

# Importing necessary modules and functions
import logging
import os
import sys
from typing import List

import pytest

# Define the base directory path and extend sys.path to include necessary directories
BASE_PATH = "/Users/silver/Logging-Toolkit"
sys.path.append(os.path.join(BASE_PATH, "src/python"))
from setup_logging import setup_logging


# Helper function to validate log content
def validate_log_content(log_path: str, expected_content: List[str]) -> None:
    """
    Validates that the specified expected content exists in the given log file.

    Parameters
    ----------
    log_path : str
        Path to the log file.
    expected_content : list of str
        List of strings expected to appear in the log file.
    """
    with open(log_path, "r", encoding="utf-8") as log_file:
        log_content = log_file.read()
        for expected in expected_content:
            assert (
                expected in log_content
            ), f"Expected '{expected}' not found in log file: {log_path}"


# Define the test function for setup_logging
def test_setup_logging():
    """
    Tests the setup_logging function for correct logger configuration and file output.
    """
    # Use test configuration files
    general_config_path = os.path.join(BASE_PATH, "src/python/general_logging.json")
    error_config_path = os.path.join(BASE_PATH, "src/python/error_logging.json")

    # Dynamically adjust the output log paths
    general_log_path = os.path.join(BASE_PATH, "logs/general.log")
    error_log_path = os.path.join(BASE_PATH, "logs/error.log")

    # Execute the setup_logging function to configure file_logger and error_logger
    file_logger = setup_logging(
        input_config_file=general_config_path,
        logger_name="general_logger",
        handler_name="general",
        output_log_path=general_log_path,
    )
    error_logger = setup_logging(
        input_config_file=error_config_path,
        logger_name="error_logger",
        handler_name="error",
        output_log_path=error_log_path,
    )

    # Test if file_logger is correctly configured
    assert file_logger is not None
    file_logger.debug("This is a DEBUG message.")
    file_logger.info("This is an INFO message.")
    file_logger.warning("This is a WARNING message.")
    file_logger.error("This is an ERROR message.")
    file_logger.critical("This is a CRITICAL message.")

    # Test if error_logger is correctly configured
    assert error_logger is not None
    error_logger.debug("This is a DEBUG message.")
    error_logger.info("This is an INFO message.")
    error_logger.warning("This is a WARNING message.")
    error_logger.error("This is an ERROR message.")
    error_logger.critical("This is a CRITICAL message.")

    # Verify log files are generated
    for log_path in [general_log_path, error_log_path]:
        assert os.path.exists(log_path), f"Log file not found: {log_path}"

    # Verify file_logger log file content
    validate_log_content(
        general_log_path,
        [
            "This is an INFO message.",
            "This is a WARNING message.",
            "This is an ERROR message.",
            "This is a CRITICAL message.",
        ],
    )

    # Verify error_logger log file content
    validate_log_content(
        error_log_path,
        [
            "This is an ERROR message.",
            "This is a CRITICAL message.",
        ],
    )

    # Clean up log files (optional)
    if os.path.exists(general_log_path):
        os.remove(general_log_path)
    if os.path.exists(error_log_path):
        os.remove(error_log_path)


# Define the test function for setup_logging and CustomLogger
def test_setup_logging_with_divider():
    """
    Tests the setup_logging function for correct logger configuration and verifies the CustomLogger addDivider functionality.
    """
    # Use test configuration files
    general_config_path = os.path.join(BASE_PATH, "src/python/general_logging.json")
    error_config_path = os.path.join(BASE_PATH, "src/python/error_logging.json")

    # Dynamically adjust the output log paths
    general_log_path = os.path.join(BASE_PATH, "logs/general.log")
    error_log_path = os.path.join(BASE_PATH, "logs/error.log")

    # Execute the setup_logging function to configure file_logger and error_logger
    file_logger = setup_logging(
        input_config_file=general_config_path,
        logger_name="general_logger",
        handler_name="general",
        output_log_path=general_log_path,
    )
    error_logger = setup_logging(
        input_config_file=error_config_path,
        logger_name="error_logger",
        handler_name="error",
        output_log_path=error_log_path,
    )

    # Test if file_logger is correctly configured
    assert file_logger is not None
    file_logger.add_divider()
    file_logger.add_divider(length=20, border="*", fill="-")
    file_logger.add_divider(level=logging.DEBUG, length=15, border="~", fill="=")

    # Test if error_logger is correctly configured
    assert error_logger is not None
    error_logger.add_divider()
    error_logger.add_divider(level=logging.ERROR, length=10, border="#", fill="~")

    # Verify log files are generated
    for log_path in [general_log_path, error_log_path]:
        assert os.path.exists(log_path), f"Log file not found: {log_path}"

    # Verify file_logger log file content
    validate_log_content(
        general_log_path,
        [
            "+==========+",
            "*--------------------*",
        ],
    )

    # Verify error_logger log file content
    validate_log_content(
        error_log_path,
        [
            "#~~~~~~~~~~#",
        ],
    )

    # Clean up log files (optional)
    if os.path.exists(general_log_path):
        os.remove(general_log_path)
    if os.path.exists(error_log_path):
        os.remove(error_log_path)


# Define the test function for log_with_borders
def test_log_with_borders():
    """
    Tests the log_with_borders method in CustomLogger for correct border formatting and message truncation.
    """
    # Use test configuration files
    general_config_path = os.path.join(BASE_PATH, "src/python/general_logging.json")
    error_config_path = os.path.join(BASE_PATH, "src/python/error_logging.json")

    # Dynamically adjust the output log paths
    general_log_path = os.path.join(BASE_PATH, "logs/general.log")
    error_log_path = os.path.join(BASE_PATH, "logs/error.log")

    # Execute the setup_logging function to configure file_logger and error_logger
    file_logger = setup_logging(
        input_config_file=general_config_path,
        logger_name="general_logger",
        handler_name="general",
        output_log_path=general_log_path,
    )
    error_logger = setup_logging(
        input_config_file=error_config_path,
        logger_name="error_logger",
        handler_name="error",
        output_log_path=error_log_path,
    )

    # Test if file_logger is correctly configured
    assert file_logger is not None
    file_logger.log_with_borders(logging.ERROR, "Another log", border="*", length=1)
    file_logger.log_with_borders(
        logging.DEBUG, "Short DEBUG message", border="|", length=20
    )
    file_logger.log_with_borders(
        logging.INFO, "Short INFO message", border="|", length=20
    )
    file_logger.log_with_borders(
        logging.WARNING,
        "This message is way too long for the specified length!",
        border="#",
        length=30,
    )

    # Test if error_logger is correctly configured
    assert error_logger is not None
    error_logger.log_with_borders(logging.ERROR, "Another log", border="*", length=1)
    error_logger.log_with_borders(
        logging.INFO, "Short INFO message", border="|", length=20
    )
    error_logger.log_with_borders(
        logging.ERROR, "Short ERROR message", border="|", length=20
    )
    error_logger.log_with_borders(
        logging.CRITICAL,
        "This message is way too long for the specified length!",
        border="#",
        length=30,
    )

    # Verify log files are generated
    for log_path in [general_log_path, error_log_path]:
        assert os.path.exists(log_path), f"Log file not found: {log_path}"

    # Verify file_logger log file content
    validate_log_content(
        general_log_path,
        [
            "* A *",
            "| Short INFO message |",
            "# This message is way too long #",
        ],
    )

    # Verify error_logger log file content
    validate_log_content(
        error_log_path,
        [
            "* A *",
            "| Short ERROR messag |",
            "# This message is way too long #",
        ],
    )

    # Clean up log files (optional)
    if os.path.exists(general_log_path):
        os.remove(general_log_path)
    if os.path.exists(error_log_path):
        os.remove(error_log_path)


# Run the test if this script is executed as the main program
if __name__ == "__main__":
    pytest.main()