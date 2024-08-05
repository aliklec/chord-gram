from sklearn.feature_extraction.text import CountVectorizer
import random

class Ngrams:
    def __init__(self, song_data):
        self.song_data = song_data
        self.ngram_counts = {}

    def get_ngrams(self, n):
        vectorizer = CountVectorizer(ngram_range=(n, n), lowercase=False, token_pattern=r'\S+')
        X = vectorizer.fit_transform(self.song_data)
        ngram_counts = X.sum(axis=0).A1
        ngram_features = vectorizer.get_feature_names_out()
        self.ngram_counts[n] = dict(zip(ngram_features, ngram_counts))
        return self.ngram_counts[n]

    def cond_probs(self, context_size):
        if context_size < 1:
            raise ValueError("context_size must be at least 1")

        context_counts = self.get_ngrams(context_size)
        target_counts = self.get_ngrams(context_size + 1)
        cond_probs = {}

        for target_sequence, target_count in target_counts.items():
            chords = target_sequence.split()
            context = ' '.join(chords[:context_size])
            if context in context_counts:
                prob = target_count / (context_counts[context] + .001)
                cond_probs[target_sequence] = prob

        return cond_probs

    def show_probs(self, context_size=2):
        cond_probs = self.cond_probs(context_size)
        for target_sequence, prob in cond_probs.items():
            chords = target_sequence.split()
            context = ' '.join(chords[:-1])
            target = chords[-1]
            print(f"P({target} | {context}) = {prob:.4f}")

    def generate_sequence(self, start_chord, sequence_length, context_size=2):
        if context_size < 1:
            raise ValueError("context_size must be at least 1")

        cond_probs = self.cond_probs(context_size)
        unigram_counts = self.get_ngrams(1)

        sequence = [start_chord]

        for _ in range(sequence_length - 1):
            current_context = ' '.join(sequence[-context_size:])
            possible_next_chords = {}

            # If we don't have enough context yet, use a partial match
            for target_sequence, prob in cond_probs.items():
                if target_sequence.endswith(current_context):
                    next_chord = target_sequence.split()[-1]
                    possible_next_chords[next_chord] = prob

            if not possible_next_chords:
                # Fall back to unigram probabilities if no matching context
                total_count = sum(unigram_counts.values())
                possible_next_chords = {chord: count / total_count for chord, count in unigram_counts.items()}

            next_chord = random.choices(list(possible_next_chords.keys()),
                                        weights=list(possible_next_chords.values()))[0]
            sequence.append(next_chord)

        return ' '.join(sequence)

# if __name__ == '__main__':
#     from db.mysql_repository import *
#     repo = MysqlRepository()
#     mychords = repo.load_chords()
#     test = Ngrams(mychords)




