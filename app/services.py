import db.mysql_repository
from model.ngrams import *

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
        return self.ngrams.generate_sequence(input_chord, 5, context_size=10)

    # FOR TESTING
    # def c_start(self):
    #     return self.ngrams.generate_sequence("C", 10, context_size=5)

if __name__ == '__main__':
    service = Services()
    # print(service.show_common_chord_combos())
    # service.show_probs()
    # chord_sequence = service.get_probable_sequence('C', 10)
    # print(chord_sequence)
    # z = service.c_start()
    # print(z)
    # print(type(z))




