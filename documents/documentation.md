# Use Cases

DRAFT

Use case 1:
Show information about common chord combinations

Use case 2:
Show probability of a chord given its context

Use case 3:
Given starting chord, generate sequence of probable chords


Other possible outputs:
- option to play audio for the full chord sequence that was generated (using Tone.js or HTML <audio>?)
- option to display notes that make up the chords
- A "generate" button that will start generating random chords and note information


# Thoughts/Future Improvements
- Smoothing/balancing to deal with different song lengths or certain songs repeating chords many times leading to overestimated probability?
- Ignore ngrams that only occur a small number of times?
- Effective ngram range for chord sequence predicton is very different from sentences. For example, the song [Riptide]([/guides/content/editing-an-existing-page](https://tabs.ultimate-guitar.com/tab/vance-joy/riptide-chords-1237247)) is made up almost entirely of repetitions of Am G C,  so for example you end up with a count of 30+ for 10 grams like "Am G C Am G C Am G C Am". Smaller ngram ranges work better. Maybe a future version would try to break up songs into "sentences" and use SOS/EOS information.
