# Logging-Toolkit

A lightweight and extensible Python logging toolkit designed for CLI tools, pipelines, and long-running batch systems.

Logging-Toolkit provides:

- A reusable `CustomLogger` with structured logging utilities
- JSON-based logging configuration
- Clean separation between logging backend and application logic
- Pipeline-friendly logging initialization

**[2026.01.28]** Major refactor and package restructuring:

- **Reorganized project as a reusable Python package (`logging_toolkit`)**
- **Separated `CustomLogger` into a dedicated module**
- **Standardized logging backend initialization via `setup_logging()`**
- **Moved logging configuration templates into `logging_toolkit/configs/`**
- **Removed legacy script-based layout (`src/python`)**
- **Prepared the project for integration as a dependency in larger systems**

**[2025.03.25]** New features added:

- **Added `log_title()`** to format structured log section titles.
- **Added `add_spacer()`** to insert blank lines for improved log readability.

**[2025.02.10]** Major update:

- **Introduced `CustomLogger`** with enhanced logging methods
- **Added `log_with_borders()`** to format logs with a bordered display
- **Enhanced `log_with_borders()` to handle multi-line messages and automatic word wrapping**
- **Added `add_divider()`** to separate log sections for better readability
- **Implemented full `pytest` testing to ensure stability**

**[2024.12.31]** Initial release of the project, including multiple logging configuration templates and a setup script.

## Installation

Logging-Toolkit is designed to be used as a **reusable Python dependency**, suitable for integration into pipeline systems, CLI tools, and research frameworks.

### Requirements

- Python **3.9 or later**

### Install as a Git submodule

This method is recommended when using Logging-Toolkit as a git submodule or a development dependency.

```bash
git submodule add git@github.com:SilverGojo4/Logging-Toolkit.git external/logging-toolkit
pip install -e external/logging-toolkit
```

### Import Usage

Once installed, Logging-Toolkit can be imported as a standard Python package:

```python
from logging_toolkit.setup_logging import setup_logging
from logging_toolkit.logger import CustomLogger
```

### Typical Usage Pattern

```python
logger = setup_logging(
    input_config_file="logging_config.json",
    logger_name="app_logger",
    handler_name="general",
    output_log_path="logs/run.log",
)

logger.info("Application started")
logger.log_title("Initialization")
```

## Design Philosophy

Logging-Toolkit is intentionally designed with the following principles:

- **No global state assumptions**
  Logging is initialized explicitly by the application entry point.

- **Configuration over code**
  Logging structure is defined via JSON configuration rather than hardcoded logic.

- **Backend-only responsibility**
  This package does not manage runtime context, pipeline state, or execution flow.

- **Framework-friendly integration**
  Designed to be embedded within CLI tools, batch systems, and pipeline runtimes.

This makes Logging-Toolkit suitable as a logging backend for larger systems rather than a standalone application.

## Features

- **Versatile Logging Configurations**: Includes JSON templates for general and error logging, easy to modify and extend.
- **Automatic Log Directory Creation**: Creates the directory if the specified log output path does not exist.
- **Explicit error surfacing**: Configuration errors are raised directly to ensure early failure and reproducibility.

### CustomLogger: Advanced Logging

Logging-Toolkit now includes a custom logger `CustomLogger`, extending Python’s built-in `logging.Logger` with additional functionality.

#### Example Usage:

- **Log messages with borders**: This method formats log messages with a bordered display for better readability.
- **Supports automatic word wrapping**: Automatically wraps long messages into multiple lines without splitting words, preventing truncation and improving readability.
- **Handles multi-line messages (`\n`)**: Preserves line breaks and formats each line properly within the bordered output.

  ```python
  logger.log_with_borders(level=logging.INFO, message="Logging Toolkit initialized!", border="*", length=30)
  logger.log_with_borders(
      level=logging.INFO,
      message="This is a very long log message that will automatically wrap.",
      border="|",
      length=30
  )
  logger.log_with_borders(level=logging.INFO, message="Line 1\nLine 2\nLine 3", border="|", length=20)
  ```

  **Output**

  ```
  * Logging Toolkit initialized!  *
  | This is a very long log    |
  | message that will          |
  | automatically wrap.        |
  | Line 1           |
  | Line 2           |
  | Line 3           |
  ```

- **Separate log sections**: Inserts visual dividers to distinguish log sections, making it easier to analyze logs in large applications.

  ```python
  logger.add_divider(level=logging.INFO, length=30, border="#", fill="~")
  ```

  **Output**

  ```
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
  ```

## Contributing

We greatly welcome contributions to Logging-Toolkit. Please submit a pull request if you have any ideas or bug fixes. We also welcome any issues you encounter while using Logging-Toolkit.

> We are particularly interested in contributions that expand support to other programming languages. Feel free to reach out if you'd like to help with implementing support for new languages.
