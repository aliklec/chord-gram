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


# Future Improvements
Smoothing/balancing to deal with different song lengths or certain songs repeating chords many times leading to overestimated probability?
Ignore ngrams that only occur a small number of times?
