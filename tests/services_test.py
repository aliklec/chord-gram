from app.services import *
from db.mysql_repository import *
import pytest

@pytest.fixture
def services():
    return Services()

def test_services_init(services):
    assert isinstance(services.repo, MysqlRepository)

def test_show_common_chord_combos(services, capsys):
    services.show_common_chord_combos()
    captured = capsys.readouterr()
    assert "Most Common" in captured.out
    assert ":" in captured.out

def test_show_probs(services, capsys):
    services.show_probs()
    captured = capsys.readouterr()
    assert "P(" in captured.out
    assert "|" in captured.out
    assert "=" in captured.out

def test_get_probable_sequence(services):
    sequence = services.get_probable_sequence("C", 5)
    assert isinstance(sequence, str)
    assert len(sequence.split()) == 5
    assert sequence.split()[0] == "C"