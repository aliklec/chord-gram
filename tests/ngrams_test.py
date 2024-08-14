import pytest
from model.ngrams import *

def test_ngrams():
    testdata = ["A B C", "E F G"]
    testgrams = Ngrams(testdata)
    assert testgrams.song_data == ["A B C", "E F G"]


def test_ngrams_data():
    testdata = [
        "A am A am",
        "A am C am",
        "A G F A",
        "G F A B",
    ]
    testgrams = Ngrams(testdata)
    ngram_counts = testgrams.get_ngrams(2)
    assert ngram_counts.get("A am", 0) == 3
    assert ngram_counts.get("F A", 0) == 2
    assert ngram_counts.get("C am", 0) == 1
    assert len(ngram_counts) == 8