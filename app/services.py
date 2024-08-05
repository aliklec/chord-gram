import db.mysql_repository
from model.ngrams import *

class Services:

    def __init__(self):
        self.repo = db.mysql_repository.MysqlRepository()
        self.chords = self.repo.load_chords()
        self.ngrams = Ngrams(self.chords)

    # Use case 1
    # Show information about common chord combinations
    def show_common_chord_combos(self, n=3, top_k=5):
        mygrams = self.ngrams.get_ngrams(n)
        sorted_grams = sorted(mygrams.items(), key=lambda item: item[1], reverse=True)

        print(f"Most Common {n}-Chord Combinations:")
        for ngram, count in sorted_grams[:top_k]:
            print(f"{ngram}: {count}")

    # Use case 2
    # Show probability of a chord given its context
    def show_probs(self, context_size=2):
        return self.ngrams.show_probs(context_size)

    # Use case 3
    # Given starting chord, generate sequence of probable chords
    def get_probable_sequence(self, start_chord, sequence_length, context_size=5):
        return self.ngrams.generate_sequence(start_chord, sequence_length, context_size)


if __name__ == '__main__':
    service = Services()
    x = service.show_common_chord_combos()
    print(x)
    service.show_probs()
    chord_sequence = service.get_probable_sequence('C', 10)
    print(chord_sequence)




