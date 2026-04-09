'''list of logger functions'''

import sys
import logging

import helper
from config.constants import PROJECT

log : logging.Logger | None = None

def get() -> logging.Logger:
    global log
    if log is None:
        log = setup()
    return log

def setup() -> logging.Logger:
    '''Setup logging format'''
    log = logging.getLogger(PROJECT)
    log_formatter = '[%(asctime)s] : %(message)s' # Syntax of the log
    date_format = '%Y-%m-%dT%H:%M:%SZ'
    formatter = logging.Formatter(log_formatter, date_format)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(formatter)
    log.addHandler(stdout_handler)
    return log

def set_log_level(log: logging.Logger):
    '''Set level log'''
    level: int = logging.DEBUG if helper.is_arg_debug() else logging.INFO
    log.setLevel(level)
    log.debug('Set debug mode')

