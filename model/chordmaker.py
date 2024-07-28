from enum import Enum
import random

# Enumerate notes
class Note(Enum):
    C = "C"
    C_SHARP = "C_SHARP"
    D = "D"
    D_SHARP = "D_SHARP"
    E = "E"
    F = "F"
    F_SHARP = "F_SHARP"
    G = "G"
    G_SHARP = "G_SHARP"
    A = "A"
    A_SHARP = "A_SHARP"
    B = "B"

# Enumerate chords
class ChordType(Enum):
    MAJ = {'maj': [0, 4, 7]}  # Major
    MIN = {'m': [0, 3, 7]}     # Minor
    DOM7 = {'7': [0, 4, 7, 10]}  # Dominant 7th
    MAJ7 = {'maj7': [0, 4, 7, 11]}  # Major 7th
    MIN7 = {'m7': [0, 3, 7, 10]}  # Minor 7th
    SUS2 = {'sus2': [0, 2, 7]}  # Suspended 2nd
    SUS4 = {'sus4': [0, 5, 7]}  # Suspended 4th
    ADD9 = {'add9': [0, 4, 7, 14]}  # Major add9
    MIN_ADD9 = {'m add9': [0, 3, 7, 14]}  # Minor add9
    DIM7 = {'dim7': [0, 3, 6, 9]} # Diminished 7th

'''
examples from data to add: 
F+ also know as F augmented (F, A, C#) 0, 4, 8
'''


class Chord:

    all_notes = list(Note)
    def __init__(self, root: Note, chord_type: ChordType, bass: Note = None):
        self.root = root
        self.chord_type = chord_type
        self.bass = bass if bass else root
        self.notes = self.create_chord()

    def create_chord(self):
        root_index = self.all_notes.index(self.root)
        intervals = list(self.chord_type.value.values())[0]
        chord_notes = [self.all_notes[(root_index + interval) % len(self.all_notes)] for interval in intervals]

        # Need to figure out if this will work for inversions too
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

# if __name__ == '__main__':
#
#     chord = Chord(Note.B, ChordType.MIN)
#     print(chord)
#
#     g_over_b = Chord(Note.G, ChordType.MAJ, bass=Note.B)
#     print(g_over_b)
#
#     random_chord = Chord.random()
#     print("RANDOM GENERATED:",random_chord)


