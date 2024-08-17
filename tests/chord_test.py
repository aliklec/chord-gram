import pytest
from model.chord import *

def test_chord():
    emin = Chord(Note.E, ChordType.MIN)
    assert emin.root == Note.E
    assert emin.chord_type == ChordType.MIN
    assert emin.notes == [Note.E, Note.G, Note.B]

    c_over_g = Chord(Note.C, ChordType.MAJ, bass=Note.G)
    assert c_over_g.root == Note.C
    assert c_over_g.bass == Note.G
    assert c_over_g.notes == [Note.G, Note.C, Note.E]

    dmaj = Chord(Note.D, ChordType.MAJ)
    notes = dmaj.create_chord()
    assert notes == [Note.D, Note.F_SHARP, Note.A]

def test_name():
    a_minor = Chord(root=Note.A, chord_type=ChordType.MIN)
    assert a_minor.name == "Am"

