'''help to manage path'''

import os
import os.path as ospath
from pathlib import Path

import logger

log = logger.get()

def get_app_path(filepath: Path) -> Path:
    '''Get path of application'''
    return Path(filepath).parent.absolute()

def get_files(folderpath: Path, format: str = ".txt") -> list[str]:
    '''Get list of files from folder'''
    return [
        f for f in os.listdir(folderpath) 
            if ospath.isfile(ospath.join(folderpath, f)) 
            and Path(f).suffix == format
        ]