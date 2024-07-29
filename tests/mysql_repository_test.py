from db.mysql_repository import *

repo = MysqlRepository()

def test_load_songs():
    mysongs = repo.load_songs()
    assert len(mysongs) == 3
    assert isinstance(mysongs, list)
    for data in mysongs:
        assert isinstance(data, dict)
    assert mysongs[0]['id'] == 1
    assert mysongs[1]['chords'] == 'C G7 G7 C C F C G7 C'
    assert mysongs[2]['url'] == 'https://tabs.ultimate-guitar.com/tab/irving-berlin/all-by-myself-chords-2762746'
