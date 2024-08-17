from app.services import *
from db.mysql_repository import *
from model.ngrams import *
from model.chord import *
import pytest


def test_services_init():
    # Initialize Services object
    services = Services()
    # Check if the repo attribute is an instance of MysqlRepository
    assert isinstance(services.repo, MysqlRepository)

def test_common_chord_combos():

    test_data = [
        "C G Am F C",
        "C G C B",
        "C G F C",
        "C G F C"
    ]
    # Initialize Services object
    s = Services()
    s.chords = test_data
    s.ngrams = Ngrams(s.chords)

    result = s.show_common_chord_combos(n=2, top_k=2)
    expected = {
        'C G': 4,
        'F C': 3
    }
    assert result == expected

def test_make_chord():
    s = Services()
    result = s.make_chord("C", "MAJ")
    assert result['notes'] == ["C", "E", "G"]