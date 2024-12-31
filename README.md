# Logging-Toolkit

This is the official codebase for configuring and setting up logging, providing a comprehensive logging solution for efficient and controlled logging in both development and production environments.

**[2024.12.31]** Initial release of the project, including multiple logging configuration templates and a setup script.

> **Note**: Currently, Logging-Toolkit supports only Python. Future updates will include support for other programming languages to make the toolkit versatile for various development environments.

## Installation and Usage

1. Ensure Python version 3.8 or later is installed.

2. Clone this repository:

   ```bash
   git clone git@github.com:SilverGojo4/Logging-Toolkit.git
   cd Logging-Toolkit
   ```

3. Use `setup_logging.py` in the `src/python` directory to configure logging:

   ```python
   from src.python.setup_logging import setup_logging

   logger = setup_logging(input_config_file="src/python/general_logging.json", logger_name="general_logger")
   logger.info("This is an info log entry.")
   ```

4. Customize the log file path (optional):

   ```python
   logger = setup_logging(input_config_file="src/python/error_logging.json", handler_name="error", output_log_path="logs/custom/error.log")
   logger.error("This is an error log entry.")
   ```

## Configuration

Logging-Toolkit includes multiple pre-configured JSON templates to simplify logging setup. Below is an overview of the provided templates:

### 1. `general_logging.json`

- **Purpose**: Logs general application messages.
- **Handlers**:
  - `console`: Outputs logs to the terminal with a simple format.
  - `general`: Writes detailed logs to `tests/python/general.log`, with support for log rotation.
- **Levels**:
  - `console`: Logs all messages starting from `DEBUG`.
  - `general`: Logs all messages starting from `INFO`.
- **Log Rotation**: Automatically rotates the log file when it exceeds 1MB, keeping up to 5 backups.

#### Example Usage:

```python
logger = setup_logging(
    input_config_file="src/python/general_logging.json",
    logger_name="general_logger"
)
logger.info("Application started.")
logger.debug("This is a debug log.")
```

### 2. `error_logging.json`

- **Purpose**: Specifically logs error-level messages for easier error tracking.
- **Handlers**:
  - `error`: Writes error logs to `tests/python/error.log`, with support for log rotation.
- **Levels**:
  - Logs all messages starting from `ERROR`.
- **Log Rotation**: Automatically rotates the log file when it exceeds 1MB, keeping up to 5 backups.

#### Example Usage:

```python
logger = setup_logging(
    input_config_file="src/python/error_logging.json",
    logger_name="error_logger"
)
logger.error("An error occurred in the application.")
```

### Customization

You can modify the provided JSON templates or create your own by adjusting:

- **Log File Path**: Update the `filename` field in the `handlers` section.
- **Log Levels**: Adjust the `level` field for handlers and loggers.
- **Log Format**: Modify the `format` and `datefmt` fields under `formatters`.

For example, to change the output path for `general.log`, provide the `output_log_path` parameter:

```python
logger = setup_logging(
    input_config_file="src/python/general_logging.json",
    handler_name="general",
    output_log_path="logs/custom/general.log"
)
logger.info("Logging to a custom path.")
```

## Features

- **Versatile Logging Configurations**: Includes JSON templates for general and error logging, easy to modify and extend.
- **Automatic Log Directory Creation**: Creates the directory if the specified log output path does not exist.
- **Detailed Error Handling**: Uses a temporary logger to record potential errors during the setup process for easy troubleshooting.

## Contributing

We greatly welcome contributions to Logging-Toolkit. Please submit a pull request if you have any ideas or bug fixes. We also welcome any issues you encounter while using Logging-Toolkit.

> We are particularly interested in contributions that expand support to other programming languages. Feel free to reach out if you'd like to help with implementing support for new languages.
