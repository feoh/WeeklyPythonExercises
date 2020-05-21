from solution import DirFileHash
from hashlib import md5
import pytest
import string
import os

@pytest.fixture
def dir_with_files(tmp_path):
    d = tmp_path

    with open(d / 'ascii_lowercase', 'w') as f:
        f.write(string.ascii_lowercase)

    with open(d / 'ascii_uppercase', 'w') as f:
        f.write(string.ascii_uppercase)

    return d

def test_hasattr_dirname():
    bad_name = '/garbage/name'
    dfh = DirFileHash(bad_name)
    assert dfh.dirname == bad_name

def test_bad_dirname():
    bad_dirname = '/garbage/dirname'
    dfh = DirFileHash(bad_dirname)
    assert dfh['abc.txt'] is None
    assert dfh[''] is None

def test_all_in_dir(dir_with_files):
    dfh = DirFileHash(dir_with_files)

    for one_filename in os.listdir(dir_with_files):
        m = md5()
        content = getattr(string, one_filename).encode()
        m.update(content)
        assert dfh[one_filename] == m.hexdigest()
