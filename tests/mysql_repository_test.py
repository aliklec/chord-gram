import pytest
from db.mysql_repository import *

repo = MysqlRepository()

def test_load_songs():
    mysongs = repo.load_songs()
    assert len(mysongs) == 30
    assert isinstance(mysongs, list)
    for data in mysongs:
        assert isinstance(data, dict)
    assert mysongs[0]['id'] == 1

def test_load_chords():
    mychords = repo.load_chords()
    assert isinstance(mychords, list)
    for each in mychords:
        assert isinstance(each, str)