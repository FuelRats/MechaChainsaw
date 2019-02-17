"""
test_mechachainsaw.py

Tests for the logging module

Copyright (c) 2018 The Fuel Rat Mischief,
All rights reserved.

Licensed under the BSD 3-Clause License.

See LICENSE.md
"""
import logging
from mechachainsaw import Logger


def test_logging_without_file():
    """
     Raise no error when not using a file.
    """
    log_handler = Logger("Test")


def test_logging_with_file():
    """
    Raise no error when specifying a filename.
    """
    log_handler = Logger("Test", logfile='Testing.log')


def test_logging_level_styles():
    """
    Raise no error when passing a custom style as dict.
    """
    custom_style = {'critical': {'color': 'red', 'bold': True},
                    'error': {'color': 'red', 'bright': True},
                    'warning': {'color': 'yellow', 'bright': True},
                    'info': {'color': 'white', 'bright': True},
                    'debug': {'color': 'black', 'bright': True}
                    }

    log_handler = Logger("testing", level_styles=custom_style)


def test_logging_field_styles():
    """
    Raise no error when passing a custom field style
    """
    custom_style = {'asctime': {'color': 'white', 'bright': True},
                    'levelname': {'color': 'white', 'bright': True},
                    'name': {'color': 'yellow', 'bright': True}}

    log_handler = Logger("testing", field_styles=custom_style)


def test_logging_demo_output(chainsaw_logger_fx):
    """
    Raise no error when running demo content
    """
    chainsaw_logger_fx.demo()


def test_custom_log_string_format():
    """
    Raise no error when using a custom log format
    """
    log_handler = Logger("testing", log_format="%(asctime)s %(name)s> %(message)s")


def test_custom_log_string_dateformat():
    """
    Raise no error when using a custom date format for the log string.
    """
    log_handler = Logger("testing", log_datefmt='%H:%M:%S')


def test_logging_default_level(chainsaw_logger_fx):
    """
    Test logging level has been set to DEBUG by default
    """
    assert chainsaw_logger_fx.getEffectiveLevel() == logging.DEBUG


def test_logging_file_default_mode(chainsaw_logger_file_fx):
    """
    Raise no error when using logfile mode 'a' (default)
    """
    chainsaw_logger_file_fx.demo()


def test_logging_file_write_mode(chainsaw_logger_file_w_fx):
    """
    Raise no error when using 'w' mode for a file to start a new one.
    """
    chainsaw_logger_file_w_fx.demo()


def test_logging_color_enable():
    """
    Raise no error when using no colors.
    """
    log_handler = Logger("testing", use_colors=False)
