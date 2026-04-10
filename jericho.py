"""Jericho"""

import logging
import sys

from os.path import join
from os import makedirs

import helper
from logger import set_log_level, log
from config import constants
import translator

from config import Config

def main():
    set_log_level(log)

    log.info("Application %s (%s) ", constants.PROJECT, constants.VERSION)
    
    app_path: str = helper.get_app_path(__file__)
    log.debug("Application path: %s", app_path)

    config_path: str = join(app_path, constants.CONFIG_PATH)
    config, _ = Config.load(config_path)
    
    config.source_directory, keep = helper.ask_folder("Choose your source folder", 
                                                     default=config.source_directory)
    if not keep:
        sys.exit(0)
    
    config.target_directory, keep = helper.ask_folder("Choose your target folder",
                                                     default=config.target_directory, 
                                                     check=False)
    if not keep:
        sys.exit(0)

    config.save()
    log.debug("%r", config.__dict__)
    
    process(config)

def process(cfg: Config):
    """Start processus to translate"""
    makedirs(cfg.target_directory, exist_ok=True)
    files: list[str] = helper.get_files(cfg.source_directory, ".txt")
    f_number: int = len(files)
    for index, file in enumerate(files):
        log.info(f"[{index+1}/{f_number}] Translating: {file}")
        src_path: str = join(cfg.source_directory, file)
        data, err = helper.read_file(src_path)
        if err:
            log.warning("reading %s: %s", src_path, err)
            continue

        translated, err = translator.translate(data)
        if err is not None:
            log.warning("translating %s: %s", src_path, err)
            continue

        dest_path: str = join(cfg.target_directory, file)
        err = helper.write_file(dest_path, translated)
        if err:
            log.warning("writing %s: %s", src_path, err)
            continue

    print("✅ All files are transltated")


if __name__ == "__main__":
    main()
