import helper
import os

testpath: str = helper.get_app_path(__file__)

def test_app_path():
    print(f'my path {testpath}\n')
    assert None != testpath

def test_get_files():
    expected: int = 4
    folder: str = os.path.join(testpath, "samples", "folder")
    files: list[str] = helper.get_files(folder)
    assert expected == len(files)

def test_read_file():
    file: str = os.path.join(testpath, "samples", "read.txt")
    data, err = helper.read_file(file)
    assert None == err
    assert None != data

def test_write_file():
    file: str = os.path.join(testpath, "samples", "read.txt")
    data, _ = helper.read_file(file)
    file: str = os.path.join(testpath, "samples", "write.txt")
    err = helper.write_file(file, data)
    assert None == err

def test_read_file_exception():
    file: str = os.path.join(testpath, "samples", "notfound.txt")
    data, err = helper.read_file(file)
    assert None != err
    assert None == data

def test_write_file_exception():
    file: str = os.path.join(testpath, "samples", "read.txt")
    data, _ = helper.read_file(file)
    file: str = os.path.join(testpath, "notfound", "write.txt")
    err = helper.write_file(file, data)
    assert None != err