import pytest
from model.scraper import *

def test_validsite():
    badsite = get_chord_data('www.test.com')
    assert badsite == None

def test_song_scrape():
    bday = get_chord_data('https://tabs.ultimate-guitar.com/tab/misc-traditional/happy-birthday-chords-1084205')
    assert bday == 'C G7 G7 C C F C G7 C'