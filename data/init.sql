CREATE DATABASE songs;

ALTER DATABASE songs CHARACTER SET latin1 COLLATE latin1_general_cs;
use songs;

CREATE TABLE song_data(
    id INT NOT NULL AUTO_INCREMENT,
    url VARCHAR(1000),
    chords TEXT,
    PRIMARY KEY (id)
);


LOAD DATA LOCAL INFILE '/docker-entrypoint-initdb.d/chords.csv'
    INTO TABLE song_data
    FIELDS TERMINATED BY ','
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS
    (url, chords);