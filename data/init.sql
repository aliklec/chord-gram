CREATE DATABASE songs;

ALTER DATABASE songs CHARACTER SET latin1 COLLATE latin1_general_cs;
use songs;

CREATE TABLE song_data(
    id INT NOT NULL AUTO_INCREMENT,
    url VARCHAR(1000),
    chords TEXT,
    PRIMARY KEY (id)
);

INSERT INTO song_data
    (url, chords)

VALUES
    ('https://tabs.ultimate-guitar.com/tab/misc-traditional/take-me-out-to-the-ball-game-chords-653035','C G C G A7 D7 Dm G G7 C G C C/B A7 F F# C A7 D7 G7 C'),
    ('https://tabs.ultimate-guitar.com/tab/misc-traditional/happy-birthday-chords-1084205','C G7 G7 C C F C G7 C'),
    ('https://tabs.ultimate-guitar.com/tab/irving-berlin/all-by-myself-chords-2762746','Bb Bbdim7 Bb Bdim F7 F+ Bb G7 Cm7 F7 Bb Bbdim7 Bb G7 C7 F7 F+ Bb C7 F7 F+ Bb Cm7 F7 Bb A7 D7 Gm C7 F7 Bb C7 F7 D7 Eb Edim Bb Fm G7 C7 F7 Bb');