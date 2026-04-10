"""Utilities module"""

import getopt
import sys
from typing import List, Tuple

SHORT_OPTIONS = 'd'
LONG_OPTIONS = ['debug']


def get_options() -> Tuple[List[Tuple[str, str]], List[str]]:
    """Get all options from console"""
    return getopt.getopt(
        sys.argv[1:], SHORT_OPTIONS, LONG_OPTIONS)


def is_arg_debug() -> bool:
    """Check if we launch into debug mode"""
    options: List[str] = ["-d", "--debug"]  # Options to check
    try:
        arguments, _ = get_options()

        for current_argument, _ in arguments:
            if current_argument in (options):
                return True
    except getopt.error:
        pass
    return False
