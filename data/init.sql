CREATE DATABASE songs;
-- MY NOTES (TO DELETE LATER)
-- utf8mb4_bin is for case sensitive sorting for unicode
-- may not need unicode for my data but need to review it first
-- figure out if i need special encoding for the song chords. for example case sensitive?
-- seems like default for 5.7 is latin case insensitive
-- see: https://planetscale.com/blog/mysql-charsets-collations
-- see: https://stackoverflow.com/questions/76148797/issue-when-migrating-data-in-charset-latin1-from-mysql-5-7-to-8-0
-- see: https://dev.mysql.com/doc/refman/5.7/en/charset-mysql.html
-- the below would be case sensitive unicode. note you need to use NVARCHAR (see video)
-- ALTER DATABASE songs CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
-- BUT I think this will work for my data:
ALTER DATABASE songs CHARACTER SET latin1 COLLATE latin1_general_cs;

CREATE TABLE song_data(
    id INT NOT NULL AUTO_INCREMENT, -- might update to include artist and song title later
    -- REMINDER: switch below to NVARCHAR if using unicode:
    url VARCHAR(1000),
    chords TEXT, -- about 65k characters
    PRIMARY KEY (id)
);

INSERT INTO songs
    (url, chords)

-- USING SAMPLE DATA FOR NOW
-- EVENTUALLY PULL FROM CSV OR DATA FILE AFTER SCRAPING
VALUES
    ('https://tabs.ultimate-guitar.com/tab/misc-traditional/take-me-out-to-the-ball-game-chords-653035','C G C G A7 D7 Dm G G7 C G C C/B A7 F F# C A7 D7 G7 C'),
    ('https://tabs.ultimate-guitar.com/tab/misc-traditional/happy-birthday-chords-1084205','C G7 G7 C C F C G7 C'),
    ('https://tabs.ultimate-guitar.com/tab/irving-berlin/all-by-myself-chords-2762746','Bb Bbdim7 Bb Bdim F7 F+ Bb G7 Cm7 F7 Bb Bbdim7 Bb G7 C7 F7 F+ Bb C7 F7 F+ Bb Cm7 F7 Bb A7 D7 Gm C7 F7 Bb C7 F7 D7 Eb Edim Bb Fm G7 C7 F7 Bb');