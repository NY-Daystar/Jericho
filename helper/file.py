'''help to manage path'''
import logger

import io
from pathlib import Path
from typing import Tuple

log = logger.get()

def read_file(filepath: Path) -> Tuple[str, Exception | None]:
    '''Read file and get its content'''
    try:
        f = io.open(filepath, mode="r", encoding="utf-8")
        content:str = f.read()
        f.close()
        return content, None
    except Exception as ex:
        log.warning(f'Except ReadFile: {ex}')
        return None, ex

def write_file(filepath: Path, data: str) -> Exception | None:
    '''Write file with data contents'''
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(data)
    except Exception as ex:
        log.warning(f'Except WriteFile: {ex}')
        return ex
    return None
    