# Chord-Gram

https://arizona.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=2cb93972-474a-4bcd-aaf3-b1cf006bc398

### Overview
Chord-gram is a program that analyzes chord data from songs. It can be used to generate n-grams based on the chord data, as well as provide information about the counts of the n-grams in order to show common chord combinations. Another feature of chord-gram is the ability to generate new chord sequences. Given a particular starting chord, chord-gram can generate a sequence of chords that are likely to follow. The program uses a database to store chord information and has a web interface that lets the user generate different chord progressions by entering a starting chord.

The code uses scikit-learn's CountVectorizer to convert the chord data into n-grams and n-gram counts. It then calculates the probabilities of chord progressions by dividing the count of the full sequence by the count of the sequence without the last chord. For example, `P(Am | C G) = Count("C G Am") / Count("C G")`. The `generate_sequence` method then uses these probabilities to create new sequences. Even using the same starting chord, a new sequence will be generated each time because the code uses Python weighted random choices, so that chords with a higher probability of following the starting chord are more likely to be selected, but there is still a degree of randomness built in.

### Data
The song data comes from Ultimate Guitar's chord pages. BeatifulSoup was used to collect the data, pulling in the source URL along with a string containing only the chords for the song. The data was then saved to a CSV file. MySQL is used to read in the CSV file and store it in a database. The current iteration of the program uses a selection of 30 songs, which can be accessed in the  `song_data` table within the MySQL `songs`  database. The code used to compile the data is found in `model\scraper.py` and can be easily modified to generate a larger dataset.

### Running the Program
To run the program, make sure you have Docker and Docker Compose installed. Clone or download the repository. Then run `docker-compose up` to build and start the containers. The application will run on http://localhost:5000. Once it is up and running you can also open the file `web/chord-gram.html` to access the User Interface. More detailed API information for chord-gram can be found in `documents/documentation.md` or at the link [here](https://github.com/aliklec/chord-gram/blob/master/documents/documentation.md).





### Challenges & Future Improvements:

In an earlier stage of the project, I created a _Chord_ object (found in _model/chordmaker.py_) with the intention of allowing the user to access more detailed information about each chord, such as its notes and the frequency of those notes. For efficiency reasons, I chose to keep the chord data as a string during n-gram generation. However, I would eventually like to update the project so that when the `/generate` API endpoint is used, each chord in the generated sequence can be mapped to a Chord object. This could allow for additional functionality such as displaying the notes found in each chord, and possibly playing the sequence out loud.

 There are limitations in the program's ability to reflect true chord progression probabilities due to the small size of the dataset and the lack of advanced smoothing techniques, which leads to overfitting. There are certain probabilities that are greatly overrepresented or underrepresented in the data. For example, the probability of seeing G after 3 occurrences of Am (found in the song [_The Only Exception_](https://tabs.ultimate-guitar.com/tab/paramore/the-only-exception-chords-874862)) is 0.99% because there is no other sequence in which a different chord appears after 3 instances of Am (note that .001 is added to the denominator when calculating probabilities, which is why it's not 100%). The probabilities are also likely affected by factors such as certain songs being much shorter or longer, and certain chord progressions that repeat many times in a single song. One example of this is the song [_Riptide_]([/guides/content/editing-an-existing-page](https://tabs.ultimate-guitar.com/tab/vance-joy/riptide-chords-1237247)), which is made up almost entirely of repetitions of Am G C. 
 
The song _The Only Exception_ and _Riptide_ also highlight another interesting limitation of the program, which is that songs are essentially treated as "sentences", which leads to various problems. Intuitively, the representation of a song as a single sentence does not seem correct, and we can see that reflected in the issues that come up. The repetitions of Am G C in _Riptide_ align with what you might call "sentences" or phrases of the song (in fact, they closely align in terms of lyrical sentences), so we can see how the overrepresentation of the Am G C progression is in part due to the incorrect classification of songs as "sentences" in the n-gram model. The example of the 99% probability of seeing G after 3 occurences of Am also seems tied to this issue of songs as sentences. In _The Only Exception_, the chorus ends with a phrase Dm Cmaj7 Am and then moves on to a new instrumental section that starts with Am Am G D. We can see here how the 3 Am's being joined together does not accurately reflect the song's syntax. For a future version of the program, it would be beneficial to perhaps break up songs into "sentences" (maybe using the song sections or line breaks that appear in Ultimate Guitar) and use start-of-sentence/end-of-sentence tags, as is often done for sentence n-gram models. For a future update, I would also like to implement more effective smoothing and balancing of the data to deal with overfitting issues. For example, one quick improvement I will test soon, is to use scikit-learn's `min_df` and `max df` to decrease the impact of n-grams that occur in most songs, or those that occur only a small number of times.

Other updates that would be useful in the future would be allowing the user to choose the n-gram context size, making the `show_probs` function more interactive (e.g. if my target is "C", what are some probable contexts for that?), and updating the code to use log probabilities to avoid numeric underflow.

### References
- Berry, Jeffrey. _sanskrit-508_ (GitHub Project). https://github.com/jjberry-508/sanskrit-508
- Borisov, Oleg (2020). _Text Generation Using N-Gram Model._ https://towardsdatascience.com/text-generation-using-n-gram-model-8d12d9802aa0
- Golotiuk, Denys (2023). _Creating a bigram language model for text generation with Python._ https://datachild.net/machinelearning/bigram-language-model-python
- Hahn-Powell, Gus. _Language models (beginner)_. https://parsertongue.org/tutorials/language-models-beginner/
- Jurafsky, D. & Martin, J. (2024). _Speech and Language Processing_. https://web.stanford.edu/~jurafsky/slp3/
- Kumaresan, Sundharesan (2024). "Cracking the Language Code: A Comprehensive Guide to N-Gram Models and Text Generation". https://medium.com/@sundharesansk11/cracking-the-language-code-a-comprehensive-guide-to-n-gram-models-and-text-generation-b670335ce6e8
