import logging

from pathlib import Path
from os.path import join
from os import makedirs
from sys import exit

import helper
import logger
import config.constants as constants
import translator

from config import Config

def main():
    log: logging.Logger = logger.get()
    logger.set_log_level(log)
    
    app_path: Path = helper.get_app_path(__file__)
   
    log.debug("Application path: %s", app_path)
    log.info("Application %s (%s) ", constants.PROJECT, constants.VERSION)

    config_path: str = join(app_path, constants.CONFIG_PATH)
    config, err = Config.load(config_path)
    if err is not None:
        log.warning("Load config: %s", err)
        config.save()
    
    config.source_directory, keep = helper.askFolder("Choose your source folder", default=config.source_directory)
    if not keep:
        exit(1)
    
    config.target_directory, keep = helper.askFolder("Choose your target folder", default=config.target_directory, check=False)
    if not keep:
        exit(1)
    config.save()
    

    log.debug("%r", config.__dict__)
    log.debug("source: %s target: %s", config.source_directory, config.target_directory)

    makedirs(config.target_directory, exist_ok=True)

    translate(config, log)

def translate(cfg: Config, log: logging.Logger): 
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
        if err != None:
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