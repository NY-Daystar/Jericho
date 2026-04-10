""" help to manage path """

__all__ = ["get_app_path", "get_files"]

import os
import os.path as ospath
from pathlib import Path
import sys

def get_app_path(call_file: str = "") -> str:
    """Get path of folder application """
    path: str
    if getattr(sys, 'frozen', False):
        path = os.path.dirname(sys.executable)
    else:
        path = os.path.dirname(os.path.abspath(call_file))
    return path

def get_files(folderpath: str, fmt: str = ".txt") -> list[str]:
    """Get list of files from folder """
    return [
        f for f in os.listdir(folderpath) if ospath.isfile(ospath.join(folderpath, f)) and Path(f).suffix == fmt
    ]
