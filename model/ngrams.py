from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import random
from model.scraper import *

# song data for testing
# song1 = get_chord_data('https://tabs.ultimate-guitar.com/tab/misc-traditional/take-me-out-to-the-ball-game-chords-653035')
# song2 = get_chord_data('https://tabs.ultimate-guitar.com/tab/misc-traditional/happy-birthday-chords-1084205')
# songs = [song1, song2]

class Ngrams:
    def __init__(self, song_data, n):
        self.song_data = song_data
        self.n = n
        self.vectorizer = CountVectorizer(ngram_range=(n, n), lowercase=False, token_pattern=r'\S+')

    def get_ngram_counts(self):
        X = self.vectorizer.fit_transform(self.song_data)
        # NOTE/REMINDER:
        # below uses numpy
        # summing counts across all songs. rows are songs, columns are ngram features
        # X.sum(axis = 0) sums columns to get ngram counts [axis 0 means columns / axis 1 means rows]
        # .A returns matrix as a numpy array, and the 1 index flattens it into a 1-dimensional array
        ngram_counts = X.sum(axis=0).A1
        ngram_features = self.vectorizer.get_feature_names_out()
        return dict(zip(ngram_features, ngram_counts))


# if __name__ == '__main__':
#     print(songs)
#     mysongdata = Ngrams(songs, 2)
#     view = mysongdata.get_ngram_counts()
#     for ngram, count in view.items():
#         print(f'{ngram}: {count}')

