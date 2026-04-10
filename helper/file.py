"""Help to manage file """

__all__ = ["read_file", "write_file"]

import io
from pathlib import Path
from typing import Tuple

from logger import log

def read_file(filepath: Path | str) -> Tuple[str | None, Exception | None]:
    """Read file and get its content """
    try:
        with io.open(filepath, mode="r", encoding="utf-8") as f:
            content:str = f.read()
            return content, None
    except Exception as ex:
        log.warning('Except ReadFile: %s', ex)
        return None, ex

def write_file(filepath: Path | str, data: str) -> Exception | None:
    """Write file with data contents """
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(data)
    except Exception as ex:
        log.warning('Except WriteFile: %s', ex)
        return ex
    return None

    