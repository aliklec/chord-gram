Project Description Goes Here





# Thoughts/Future Improvements
- Smoothing/balancing to deal with different song lengths or certain songs repeating chords many times leading to overestimated probability?
- Ignore ngrams that only occur a small number of times?
- Effective ngram range for chord sequence predicton is very different from sentences. For example, the song [Riptide]([/guides/content/editing-an-existing-page](https://tabs.ultimate-guitar.com/tab/vance-joy/riptide-chords-1237247)) is made up almost entirely of repetitions of Am G C,  so for example you end up with a count of 30+ for 10 grams like "Am G C Am G C Am G C Am". Smaller ngram ranges work better. Maybe a future version would try to break up songs into "sentences" and use SOS/EOS information.
- Currently only using a small sample selection of song data (around 30 songs) so will be interesting to see how things look with a larger dataset

