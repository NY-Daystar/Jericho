"""Jericho """

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
    log.info("Application %s (%s)\n%s", constants.PROJECT, constants.VERSION, constants.DESCRIPTION)
    app_path: str = helper.get_app_path(__file__)
    log.debug("Application path: %s", app_path)

    config_path: str = join(app_path, constants.CONFIG_PATH)
    log.debug("Configuration path: %s", config_path)
    cfg, _ = Config.load(config_path)
    cfg.source_directory, keep = helper.ask_folder("Choose your source folder (put absolute path)", default=cfg.source_directory)
    if keep:
        makedirs(cfg.source_directory, exist_ok=True)
    else:
        sys.exit(0)
    
    cfg.target_directory, _ = helper.ask_folder("Choose your target folder (put absolute path)", default=cfg.target_directory, check=False)
    cfg.save()
    process(cfg)
    wait()

def process(cfg: Config):
    """Start processus to translate """
    log.debug("%r", cfg.__dict__)
    makedirs(cfg.target_directory, exist_ok=True)

    files: list[str] = helper.get_files(cfg.source_directory, ".txt")
    f_number: int = len(files)
    for index, file in enumerate(files):
        log.info("[%d/%d] Translating: %s", index+1, f_number, file)
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

    print("✅ All files are translated")

def wait():
    """Wait the end of program ask user to press enter """
    print("Press enter to exit program\n")
    scan = sys.stdin.read(1)
    return scan == "\n"


if __name__ == "__main__":
    main()
