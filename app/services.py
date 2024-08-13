import db.mysql_repository
from model.ngrams import *
from model.chordmaker import *

class Services:

    def __init__(self):
        self.repo = db.mysql_repository.MysqlRepository()
        self.chords = self.repo.load_chords()
        self.ngrams = Ngrams(self.chords)

    # Use case 1
    # Show information about common chord combinations
    def show_common_chord_combos(self, n=3, top_k=10):
        mygrams = self.ngrams.get_ngrams(n)
        sorted_grams = sorted(mygrams.items(), key=lambda item: item[1], reverse=True)

        result = {}
        for ngram, count in sorted_grams[:top_k]:
            result[ngram] = int(count)

        return result

    # Use case 2
    # Given starting chord, generate a sequence of probable chords
    def make_sequence(self, input_chord: str):
        return self.ngrams.generate_sequence(input_chord, 10, context_size=10)

    # FOR TESTING
    # def c_start(self):
    #     return self.ngrams.generate_sequence("C", 10, context_size=5)

    # IN DEVELOPMENT


    def make_chord(self, root: str, chord_type: str, bass: str = None):
        try:
            root_note = Note[root.upper().replace('#', '_SHARP')]
            chord_type_enum = ChordType[chord_type.upper()]
            bass_note = Note[bass.upper().replace('#', '_SHARP')] if bass else None

            chord = Chord(root_note, chord_type_enum, bass_note)

            return {
                "name": chord.name,
                "notes": [note.value for note in chord.notes]
            }
        except KeyError as e:
            return {"error": f"Invalid input: {str(e)}"}

# if __name__ == '__main__':
#     service = Services()
#     print(service.show_common_chord_combos())
#     # print(service.c_start())
#     print(service.make_sequence("Am"))




