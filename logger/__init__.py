"""list of logger functions."""

__all__ = ["set_log_level", "log"]

import sys
import logging

import helper
from config.constants import PROJECT

log : logging.Logger | None = None

def setup() -> logging.Logger:
    """
    setup : initialize logging format
    """
    logger: logging.Logger = logging.getLogger(PROJECT)
    log_formatter = '[%(asctime)s] : %(message)s' # Syntax of the log
    date_format = '%Y-%m-%dT%H:%M:%SZ'
    formatter = logging.Formatter(log_formatter, date_format)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(formatter)
    logger.addHandler(stdout_handler)
    return logger

def set_log_level(logger: logging.Logger):
    """
    Set level log
    """
    level: int = logging.DEBUG if helper.is_arg_debug() else logging.INFO
    logger.setLevel(level)
    logger.debug('Set debug mode')

if log is None:
    log = setup()