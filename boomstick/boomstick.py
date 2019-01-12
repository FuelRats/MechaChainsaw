"""
boomstick.py - Logging engine

Copyright (c) 2018 The Fuel Rat Mischief,
All rights reserved.

Licensed under the BSD 3-Clause License.

See LICENSE.MD
"""

import logging
import coloredlogs


class Logger:

    def __init__(self, logfile: str):
        self.log = logging.getLogger(f"{__name__}")

        # create a handler for said logger...
        file_logger = logging.FileHandler(logfile, 'a', encoding="utf-8")
        log_format = '<%(asctime)s %(name)s> [%(levelname)s] %(message)s'
        log_datefmt = '%Y-%m-%d %H:%M:%S'
        file_logger_format = logging.Formatter(log_format)

        # set the formatter to actually use it
        file_logger.setFormatter(file_logger_format)

        # add the handler to the log.
        logging.getLogger(f"{__name__}").addHandler(file_logger)

        # set proper severity level
        self.log.setLevel(10)

        # add Console logging
        console = logging.StreamHandler()
        logging.getLogger(f"{__name__}").addHandler(console)

        # add console logging format
        console_format = logging.Formatter(log_format)

        # set console formatter to use our format.
        console.setFormatter(console_format)

        # coloredlogs hook
        log_levelstyles = {'critical': {'color': 'red', 'bold': True},
                           'error': {'color': 'red', 'bright': True},
                           'warning': {'color': 'yellow', 'bright': True},
                           'info': {'color': 'white', 'bright': True},
                           'debug': {'color': 'black', 'bright': True}}

        log_fieldstyles = {'asctime': {'color': 'white', 'bright': True},
                           'levelname': {'color': 'white', 'bright': True},
                           'name': {'color': 'yellow', 'bright': True}}

        # coloredlogs hook
        coloredlogs.install(handler=f"{__name__}",
                            level='a',
                            fmt=log_format,
                            level_styles=log_levelstyles,
                            field_styles=log_fieldstyles,
                            datefmt=log_datefmt,
                            isatty=True,
                            )

        # disable propagation
        self.log.propagate = False

        self.log.info("Boomstick Loaded and ready for logging.")
