# Chord-Gram

### Overview
Chord-gram is a program that analyzes chord data from songs. It can be used to generate n-grams based on chord data. It can then analyze the counts of those n-grams and display information such as common chord combinations and probabilities of a chord given the context.

### Data
The song data comes from Ultimate Guitar's chord pages. The current iteration of the program uses a selection of 30 songs, which can be found in chords.csv within the Data directory. 

### The code




### Challenges/Future Improvements:
- Smoothing/balancing to deal with different song lengths or certain songs repeating chords many times leading to overestimated probability?
- Ignore ngrams that only occur a small number of times?
- Effective ngram range for chord sequence predicton is very different from sentences. For example, the song [Riptide]([/guides/content/editing-an-existing-page](https://tabs.ultimate-guitar.com/tab/vance-joy/riptide-chords-1237247)) is made up almost entirely of repetitions of Am G C,  so for example you end up with a count of 30+ for 10 grams like "Am G C Am G C Am G C Am". Smaller ngram ranges work better. Maybe a future version would try to break up songs into "sentences" and use SOS/EOS information.
- Currently, the project uses only a small sample selection of 30 songs for the chord data, so it will be interesting to see how things look with a larger dataset
- Update the show_probs function to make it more interactive. E.g., if my target is C, what are some probable contexts for that.
- More features to visualize the n-grams. 

# References
- Jurafsky and Martin
- Jeffrey Berry's sanskrit-508 project: https://github.com/jjberry-508/sanskrit-508/
- https://medium.com/@sundharesansk11/cracking-the-language-code-a-comprehensive-guide-to-n-gram-models-and-text-generation-b670335ce6e8
- https://cs-114.org/wp-content/uploads/2016/02/CS114_L5_NgramModels.pdf