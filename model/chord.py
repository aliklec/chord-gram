from enum import Enum
import random

# Enumerate notes
# UPDATE TO INCLUDE NOTE FREQUENCY INFO
class Note(Enum):
    C = "C"
    C_SHARP = "C#"
    D = "D"
    D_SHARP = "D#"
    E = "E"
    F = "F"
    F_SHARP = "F#"
    G = "G"
    G_SHARP = "G#"
    A = "A"
    A_SHARP = "A#"
    B = "B"

# Enumerate chords
class ChordType(Enum):
    MAJ = {'': [0, 4, 7]}  # Major
    MIN = {'m': [0, 3, 7]}     # Minor
    DOM7 = {'7': [0, 4, 7, 10]}  # Dominant 7th
    MAJ7 = {'maj7': [0, 4, 7, 11]}  # Major 7th
    MIN7 = {'m7': [0, 3, 7, 10]}  # Minor 7th
    SUS2 = {'sus2': [0, 2, 7]}  # Suspended 2nd
    SUS4 = {'sus4': [0, 5, 7]}  # Suspended 4th
    ADD9 = {'add9': [0, 4, 7, 14]}  # Major add9
    MIN_ADD9 = {'m add9': [0, 3, 7, 14]}  # Minor add9
    DIM7 = {'dim7': [0, 3, 6, 9]} # Diminished 7th

    # to test or add:
    # 6sus2 [0 2 7 9] as in D6sus2
    # 6 chord [0 3 7 9] as in Fm6
    # add11 [0 4 7 17]
    # add4 [0 4 5 7]
    # 7sus4 [0 5 7 10]
    # F+ aka F augmented (F, A, C#) [0, 4, 8]

class Chord:

    all_notes = list(Note)
    def __init__(self, root: Note, chord_type: ChordType, bass: Note = None):
        self.root = root
        self.chord_type = chord_type
        self.bass = bass if bass else root
        self.notes = self.create_chord()

    def create_chord(self):
        # find index of root note
        root_index = self.all_notes.index(self.root)
        # get intervals from the chord type enum
        intervals = list(self.chord_type.value.values())[0]
        # create list of notes - iterate through the intervals for the type of chord
        chord_notes = []
        for interval in intervals:
            # use % to wrap around if we get through all notes
            index = (root_index + interval) % len(self.all_notes)
            note = self.all_notes[index]
            chord_notes.append(note)

        # Note to self - need to check out inversions
        if self.bass != self.root:
            # Move bass note to the bottom
            chord_notes = [self.bass] + [note for note in chord_notes if note != self.bass]
        return chord_notes

    @property
    def name(self) -> str:
        chord_symbol = list(self.chord_type.value.keys())[0]
        if self.bass == self.root:
            return f"{self.root.value}{chord_symbol}"
        else:
            return f"{self.root.value}{chord_symbol}/{self.bass.value}"

    def __str__(self) -> str:
        return f"{self.name}: {[note.value for note in self.notes]}"

    # Random generator just fun but not needed for project
    @classmethod
    def random(cls):
        root = random.choice(cls.all_notes)
        chord_type = random.choice(list(ChordType))
        return cls(root, chord_type)

if __name__ == '__main__':

    chord = Chord(Note.B, ChordType.MIN)
    print(chord)

    g_over_b = Chord(Note.G, ChordType.MAJ, bass=Note.B)
    print(g_over_b)

    random_chord = Chord.random()
    print("RANDOM GENERATED:",random_chord)


