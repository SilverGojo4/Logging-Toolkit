# pylint: disable=
"""
Custom logger implementation.

This module defines the CustomLogger class, which extends Python's
built-in logging.Logger with additional utilities for structured,
readable, and pipeline-friendly logging output.
"""

from __future__ import annotations

# Standard Library Imports
import datetime
import logging
import os
import platform
import sys
import textwrap


class CustomLogger(logging.Logger):
    """
    Extended logger with structured formatting utilities.

    This logger enhances the standard logging.Logger by providing
    additional helper methods designed for long-running pipelines,
    research workflows, and CLI-based execution environments.

    Features
    --------
    - Structured visual dividers
    - Section titles
    - Multi-line bordered messages
    - Pipeline initialization summaries
    - Improved readability for long logs

    Notes
    -----
    This class does NOT configure handlers, formatters, or log files.
    It only defines logging behaviors.
    """

    def add_spacer(
        self,
        level: int = logging.INFO,
        lines: int = 1,
    ) -> None:
        """
        Insert empty spacer lines into the log output.

        Parameters
        ----------
        level : int, optional
            Logging level to emit spacer lines.
        lines : int, optional
            Number of empty lines to insert.
        """
        lines = max(lines, 1)

        for _ in range(lines):
            self.log(level, " ")

    def add_divider(
        self,
        level: int = logging.INFO,
        length: int = 10,
        border: str = "+",
        fill: str = "=",
    ) -> None:
        """
        Insert a visual divider into the log output.

        Parameters
        ----------
        level : int
            Logging level.
        length : int
            Total divider length.
        border : str
            Character used at divider edges.
        fill : str
            Character used for divider body.
        """
        length = max(length, 3)
        divider = f"{border}{fill * (length - 2)}{border}"
        self.log(level, divider)

    def log_with_borders(
        self,
        level: int,
        message: str,
        border: str = "|",
        length: int = 50,
    ) -> None:
        """
        Log a message surrounded by vertical borders.

        The message supports multi-line input and automatic
        word wrapping without breaking words.

        Parameters
        ----------
        level : int
            Logging level.
        message : str
            Message to log.
        border : str
            Border character.
        length : int
            Total width of the bordered output.
        """
        length = max(length, 5)
        max_message_length = length - 4

        message_lines = message.splitlines()

        wrapped_lines = []
        for line in message_lines:
            wrapped_lines.extend(textwrap.wrap(line, width=max_message_length) or [""])

        for line in wrapped_lines:
            formatted = f"{border} {line.ljust(max_message_length)} {border}"
            self.log(level, formatted)

    def log_title(
        self,
        title: str,
        level: int = logging.INFO,
        length: int = 40,
        border: str = "#",
    ) -> None:
        """
        Log a formatted section title.

        Parameters
        ----------
        title : str
            Section title text.
        level : int
            Logging level.
        length : int
            Number of border characters on each side.
        border : str
            Border character.
        """
        formatted = f"{border * length} {title} {border * length}"
        self.log(level, formatted)

    def log_pipeline_initialization(
        self,
        project_name: str,
        level: int = logging.INFO,
        line_width: int = 100,
        border: str = "║",
    ) -> None:
        """
        Log pipeline execution metadata in a structured block.

        Parameters
        ----------
        project_name : str
            Pipeline or project name.
        level : int
            Logging level.
        line_width : int
            Width of the bordered block.
        border : str
            Border character.
        """
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        metadata_lines = [
            f"Project Name      : '{project_name}'",
            f"Working Directory : '{os.getcwd()}'",
            f"Platform          : '{platform.system()}'",
            f"Execution Time    : {now}",
            f"Python Version    : {sys.version.split()[0]}",
        ]

        cli_lines = ["", "CLI command used:"]
        cli_lines.append(f"python {sys.argv[0]} \\")

        i = 1
        while i < len(sys.argv):
            if (
                sys.argv[i].startswith("-")
                and i + 1 < len(sys.argv)
                and not sys.argv[i + 1].startswith("-")
            ):
                cli_lines.append(f"  {sys.argv[i]} {sys.argv[i + 1]} \\")
                i += 2
            else:
                cli_lines.append(f"  {sys.argv[i]} \\")
                i += 1

        if cli_lines[-1].endswith(" \\"):
            cli_lines[-1] = cli_lines[-1][:-2]

        self.add_divider(level=level, length=line_width, border="+", fill="=")
        self.log_with_borders(
            level=level,
            message="\n".join(metadata_lines + cli_lines),
            border=border,
            length=line_width,
        )
        self.add_divider(level=level, length=line_width, border="+", fill="=")
