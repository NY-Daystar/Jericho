"""poetry run pytest tests/helper_test.py"""

import os

import helper

testpath: str = helper.get_app_path(__file__)

def test_app_path():
    print(f'my path {testpath}\n')
    assert None != testpath

def test_get_files():
    expected: int = 4
    folder: str = os.path.join(testpath, "samples", "folder")
    files: list[str] = helper.get_files(folder)
    assert len(files) == expected

def test_read_file():
    file: str = os.path.join(testpath, "samples", "read.txt")
    data, err = helper.read_file(file)
    assert err == None
    assert data != None

def test_write_file():
    file: str = os.path.join(testpath, "samples", "read.txt")
    data, _ = helper.read_file(file)
    file: str = os.path.join(testpath, "samples", "write.txt")
    err = helper.write_file(file, data)
    assert err == None

def test_read_file_exception():
    file: str = os.path.join(testpath, "samples", "notfound.txt")
    data, err = helper.read_file(file)
    assert err != None
    assert data == None

def test_write_file_exception():
    file: str = os.path.join(testpath, "samples", "read.txt")
    data, _ = helper.read_file(file)
    file: str = os.path.join(testpath, "notfound", "write.txt")
    err = helper.write_file(file, data)
    assert err != None
