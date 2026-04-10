"""Config of Jericho"""

import json
import os
from typing import Tuple

from .constants import DEFAULT_DEBUG, DEFAULT_SOURCE_DIR, DEFAULT_TARGET_DIR

class Config:
    """Config of the application"""
    path: str
    debug: str
    source_directory: str
    target_directory: str

    def __init__(self, path, debug, source_directory, target_directory):
        self.path = path
        self.debug = debug
        self.source_directory = source_directory
        self.target_directory = target_directory

    def save(self):
        """Save config into the path define"""
        with open(self.path, 'w', encoding="utf-8") as document:
            json.dump(self.to_dict(), document, indent=4)

    @classmethod
    def load(cls, filepath: str) -> Tuple[Config, Exception]:
        """Create config object loading data from config.json file"""
        default: Config = cls(path=filepath, debug=DEFAULT_DEBUG,
                    source_directory=DEFAULT_SOURCE_DIR, target_directory=DEFAULT_TARGET_DIR)

        if not os.path.exists(filepath):
            return default, FileNotFoundError(filepath)

        try:
            with open(filepath, mode='r', encoding='utf-8') as document:
                data = json.load(document)
                return cls(
                    path=filepath,
                    debug=data.get("debug", DEFAULT_DEBUG),
                    source_directory=data.get("source", DEFAULT_SOURCE_DIR),
                    target_directory=data.get("target", DEFAULT_TARGET_DIR),
                ), None
        except Exception as ex:
            return None, ex
    
    def to_dict(self):
        return {
            "debug": self.debug,
            "source": self.source_directory,
            "target": self.target_directory,
        }
