"""Logger module """

__all__ = ["set_log_level", "log"]

import getopt
import logging
import sys
from typing import List, Tuple

from config.constants import PROJECT

SHORT_OPTIONS = 'd'
LONG_OPTIONS = ['debug']

log : logging.Logger
created : bool = False

def setup() -> logging.Logger:
    """Setup : initialize logging format """
    logger: logging.Logger = logging.getLogger(PROJECT)
    log_formatter = '[%(asctime)s] : %(message)s' # Syntax of the log
    date_format = '%Y-%m-%dT%H:%M:%SZ'
    formatter = logging.Formatter(log_formatter, date_format)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(formatter)
    logger.addHandler(stdout_handler)
    return logger

def set_log_level(logger: logging.Logger):
    """Set level log """
    level: int = logging.DEBUG if is_arg_debug() else logging.INFO
    logger.setLevel(level)
    logger.debug('Set debug mode')

def is_arg_debug() -> bool:
    """ Check if we launch into debug mode """
    options: List[str] = ["-d", "--debug"]  # Options to check
    try:
        arguments, _ = get_options()

        for current_argument, _ in arguments:
            if current_argument in (options):
                return True
    except getopt.error:
        pass
    return False

def get_options() -> Tuple[List[Tuple[str, str]], List[str]]:
    """ Get all options from console """
    return getopt.getopt(
        sys.argv[1:], SHORT_OPTIONS, LONG_OPTIONS)


if not created:
    log = setup()