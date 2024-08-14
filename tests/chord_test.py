import pytest
from model.chord import *

def test_chord():
    cmaj = Chord(Note.C, ChordType.MAJ)
    assert cmaj.root == Note.C
    assert cmaj.chord_type == ChordType.MAJ
    assert cmaj.bass == Note.C
    assert cmaj.notes == [Note.C, Note.E, Note.G]

    c_over_g = Chord(Note.C, ChordType.MAJ, bass=Note.G)
    assert c_over_g.root == Note.C
    assert c_over_g.bass == Note.G
    assert c_over_g.notes == [Note.G, Note.C, Note.E]

def test_create_chord():
    bmin = Chord(Note.B, ChordType.MIN)
    notes = bmin.create_chord()
    assert notes == [Note.B, Note.D, Note.F_SHARP]

def test_name():
    a_minor = Chord(root=Note.A, chord_type=ChordType.MIN)
    assert a_minor.name == "Am"

