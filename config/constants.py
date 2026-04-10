"""Constants for Jericho projects """

__all__ = ["PROJECT", "VERSION", "DESCRIPTION", "CONFIG_PATH", "DEFAULT_DEBUG", "DEFAULT_SOURCE_DIR", "DEFAULT_TARGET_DIR"]

PROJECT: str = 'Jericho'
VERSION: str = 'v0.2.0'
DESCRIPTION: str = 'tool to translate english files to french files'

# Configuration
CONFIG_PATH: str = 'config.json'
DEFAULT_DEBUG: str = 'true'
DEFAULT_SOURCE_DIR: str = 'data/source'
DEFAULT_TARGET_DIR: str = 'data/target'
