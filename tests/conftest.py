"""
conftest.py - PyTest fixtures.

Copyright (c) 2018 The Fuel Rats Mischief,
All rights reserved.

Licensed under the BSD 3-Clause License.

See LICENSE
"""
from mechachainsaw import Logger

import pytest


@pytest.fixture
def chainsaw_logger_fx() -> Logger:
    return Logger("Testing")


@pytest.fixture
def chainsaw_logger_file_fx() -> Logger:
    return Logger("File_Testing", logfile="testing.log", logfile_mode='a')


@pytest.fixture
def chainsaw_logger_file_w_fx() -> Logger:
    return Logger("File_Testing_w", logfile="testing_w.log", logfile_mode='w')
