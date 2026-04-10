"""poetry run pytest tests/config_test.py"""

import os
import helper

from pathlib import Path

from config import Config


testpath: str = helper.get_app_path(__file__)
rootpath: str = Path(__file__).parents[0].parent


def test_read_configuration():
    cfg, err = Config.load(os.path.join(rootpath, "config.example.json"))
    print(f"configuration loaded : {cfg.__dict__}")

    assert cfg.path != None
    assert err == None

def test_save_configuration():
    # Arrange
    cfgpath:str = os.path.join(testpath, "samples", "config_test.json")
    if os.path.exists(cfgpath):
        os.remove(cfgpath)

    # Act
    cfg, _ = Config.load(os.path.join(rootpath, "config.example.json"))
    cfg.path = cfgpath
    cfg.save()

    # Assert
    assert os.path.exists(cfg.path)

def test_bad_configuration():
    # Arrange
    cfgpath:str = os.path.join(testpath, "samples", "bad_config.json")

    # Act
    cfg, err = Config.load(cfgpath)
   
    # Assert
    assert cfg == None
    assert err != None
