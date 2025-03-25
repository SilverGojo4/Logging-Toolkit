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
            "+========+",
            "*------------------*",
        ],
    )

    # Verify error_logger log file content
    validate_log_content(
        error_log_path,
        [
            "#~~~~~~~~#",
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

    # Ensure loggers are correctly initialized
    assert file_logger is not None
    assert error_logger is not None

    # Test if file_logger is correctly configured
    file_logger.log_with_borders(
        level=logging.INFO, message="Hello", border="|", length=10
    )  ### 1. Single-line message
    file_logger.log_with_borders(
        level=logging.INFO, message="Hi", border="|", length=1
    )  ### 2. Short message (minimum length = 1)
    file_logger.log_with_borders(
        level=logging.WARNING,
        message="This is a long test message that should wrap correctly.",
        border="#",
        length=20,
    )  ### 3. Long message wrapping test
    file_logger.log_with_borders(
        level=logging.INFO,
        message="Line 1\nLine 2\nLine 3",
        border="|",
        length=15,
    )  ### 4. Message containing newline characters (`\n`)
    file_logger.log_with_borders(
        level=logging.INFO,
        message="Hello\n\nWorld",
        border="|",
        length=10,
    )  ### 5. Message containing empty lines (`\n\n`)
    file_logger.log_with_borders(
        level=logging.INFO,
        message="Supercalifragilisticexpialidocious",
        border="|",
        length=10,
    )  ### 6. Single word longer than `length`
    file_logger.log_with_borders(
        level=logging.INFO, message="Custom border", border="@", length=20
    )  ### 7. Custom border characters
    file_logger.log_with_borders(
        level=logging.DEBUG, message="", border="*", length=10
    )  ### 8. Edge case: Empty string

    # Test if error_logger is correctly configured
    error_logger.log_with_borders(logging.ERROR, "Log", border="*", length=1)
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
    error_logger.log_with_borders(
        level=logging.CRITICAL,
        message="Hello\n\nWorld",
        border="|",
        length=10,
    )

    # Verify log files are generated
    for log_path in [general_log_path, error_log_path]:
        assert os.path.exists(log_path), f"Log file not found: {log_path}"

    # Verify file_logger log file content
    validate_log_content(
        general_log_path,
        [
            "| Hello  |",
            "| H |",
            "| i |",
            "# This is a long   #",
            "# test message     #",
            "# that should wrap #",
            "# correctly.       #",
            "| Line 1      |",
            "| Line 2      |",
            "| Line 3      |",
            "| Hello  |",
            "|        |",
            "| World  |",
            "| Superc |",
            "| alifra |",
            "| gilist |",
            "| icexpi |",
            "| alidoc |",
            "| ious   |",
            "@ Custom border    @",
        ],
    )

    # Verify error_logger log file content
    validate_log_content(
        error_log_path,
        [
            "* L *",
            "* o *",
            "* g *",
            "| Short ERROR      |",
            "| message          |",
            "# This message is way too    #",
            "# long for the specified     #",
            "# length!                    #",
            "| Hello  |",
            "|        |",
            "| World  |",
        ],
    )

    # Clean up log files (optional)
    if os.path.exists(general_log_path):
        os.remove(general_log_path)
    if os.path.exists(error_log_path):
        os.remove(error_log_path)


# Define the test function for add_spacer
def test_add_spacer():
    """
    Tests the add_spacer method in CustomLogger to ensure correct spacing in the log output.
    """
    # Use test configuration files
    general_config_path = os.path.join(BASE_PATH, "src/python/general_logging.json")
    general_log_path = os.path.join(BASE_PATH, "logs/general.log")

    # Execute the setup_logging function to configure file_logger
    file_logger = setup_logging(
        input_config_file=general_config_path,
        logger_name="general_logger",
        handler_name="general",
        output_log_path=general_log_path,
    )

    # Ensure file_logger is correctly configured
    assert file_logger is not None

    # Test add_spacer functionality
    file_logger.info("Step 1: Data Preprocessing")
    file_logger.add_spacer()  # Insert 1 empty line
    file_logger.info("Step 2: Model Training")
    file_logger.add_spacer(lines=2)  # Insert 2 empty lines
    file_logger.info("Step 3: Model Evaluation")
    file_logger.add_spacer(lines=3)  # Insert 3 empty lines
    file_logger.info("Final Step: Report Generation")

    # Verify log files are generated
    assert os.path.exists(general_log_path), f"Log file not found: {general_log_path}"

    # Verify log file content
    validate_log_content(
        general_log_path,
        [
            "Step 1: Data Preprocessing",
            "",
            "Step 2: Model Training",
            "",
            "",
            "Step 3: Model Evaluation",
            "",
            "",
            "",
            "Final Step: Report Generation",
        ],
    )

    # Clean up log file (optional)
    if os.path.exists(general_log_path):
        os.remove(general_log_path)


# Define the test function for log_title
def test_log_title():
    """
    Tests the log_title method in CustomLogger to ensure correct formatted title output.
    """
    # Use test configuration files
    general_config_path = os.path.join(BASE_PATH, "src/python/general_logging.json")
    general_log_path = os.path.join(BASE_PATH, "logs/general.log")

    # Execute the setup_logging function to configure file_logger
    file_logger = setup_logging(
        input_config_file=general_config_path,
        logger_name="general_logger",
        handler_name="general",
        output_log_path=general_log_path,
    )

    # Ensure file_logger is correctly configured
    assert file_logger is not None

    # Test log_title functionality
    file_logger.log_title("AMP - Data Collect")
    file_logger.log_title("Processing Data", length=30, border="*")
    file_logger.log_title("Training Model", length=25, border="=")

    # Verify log files are generated
    assert os.path.exists(general_log_path), f"Log file not found: {general_log_path}"

    # Verify file_logger log file content
    validate_log_content(
        general_log_path,
        [
            "#" * 40 + " 'AMP - Data Collect' " + "#" * 40,
            "*" * 30 + " 'Processing Data' " + "*" * 30,
            "=" * 25 + " 'Training Model' " + "=" * 25,
        ],
    )

    # Clean up log file (optional)
    if os.path.exists(general_log_path):
        os.remove(general_log_path)


# Run the test if this script is executed as the main program
if __name__ == "__main__":
    pytest.main()
