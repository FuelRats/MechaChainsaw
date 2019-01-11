"""
boomstick.py - Logging engine

Copyright (c) 2018 The Fuel Rat Mischief,
All rights reserved.

Licensed under the BSD 3-Clause License.

See LICENSE.MD
"""

import logging
import coloredlogs


class Boomstick:

    LOG = logging.getLogger()

    def setup_logging(self, logfile: str):
        _LOG_LEVEL = logging.DEBUG

        #####
        # File Handler
        ###

        file_logger = logging.FileHandler(logfile, 'a', encoding='utf-8')
        log_format = '<%(asctime)s %(name)s> [%(levelname)s] %(message)s'
        log_datefmt = '%Y-%m-%d %H:%M:%S'
        file_logger_format = logging.Formatter(log_format)
        file_logger.setFormatter(log_format)
        logging.getLogger().addHandler(log_format)
        Boomstick.LOG.setLevel(_LOG_LEVEL)

        #####
        # Console Handler
        ###
        console = logging.StreamHandler()
        logging.getLogger().addHandler(console)

        #####
        # ColoredLogs hooks
        ###
        log_levelstyles = {'critical': {'color': 'red', 'bold': True},
                           'error': {'color': 'red', 'bright': True},
                           'warning': {'color': 'yellow', 'bright': True},
                           'info': {'color': 'white', 'bright': True},
                           'debug': {'color': 'black', 'bright': True}}

        log_fieldstyles = {'asctime': {'color': 'white', 'bright': True},
                           'levelname': {'color': 'white', 'bright': True},
                           'name': {'color': 'yellow', 'bright': True}}

        # coloredlogs hook
        coloredlogs.install(handler=__name__,
                            level=_LOG_LEVEL,
                            fmt=log_format,
                            level_styles=log_levelstyles,
                            field_styles=log_fieldstyles,
                            datefmt=log_datefmt,
                            isatty=True,
                            )

        # disable propagation
        self.LOG.propagate = False

        Boomstick.LOG.info(f"[Boomstick] Logging started.")

    def demo(self):
        self.LOG.debug("[Boomstick Demo] This is a Debug Entry.")
        self.LOG.info("[Boomstick Demo] This is an Info Entry.")
        self.LOG.warning("[Boomstick Demo] This is a Warning Entry.")
        self.LOG.error("[Boomstick Demo] This is an Error Entry.")
