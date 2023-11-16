DROP TABLE album CASCADE;
CREATE TABLE album (
    id SERIAL,
    title VARCHAR(128) UNIQUE,
    PRIMARY KEY(id)
);

DROP TABLE track CASCADE;
CREATE TABLE track (
    id SERIAL,
    title TEXT, 
    artist TEXT, 
    album TEXT, 
    album_id INTEGER REFERENCES album(id) ON DELETE CASCADE,
    count INTEGER, 
    rating INTEGER, 
    len INTEGER,
    PRIMARY KEY(id)
);

DROP TABLE artist CASCADE;
CREATE TABLE artist (
    id SERIAL,
    name VARCHAR(128) UNIQUE,
    PRIMARY KEY(id)
);

DROP TABLE tracktoartist CASCADE;
CREATE TABLE tracktoartist (
    id SERIAL,
    track VARCHAR(128),
    track_id INTEGER REFERENCES track(id) ON DELETE CASCADE,
    artist VARCHAR(128),
    artist_id INTEGER REFERENCES artist(id) ON DELETE CASCADE,
    PRIMARY KEY(id)
);

\copy track(title,artist,album,count,rating,len) FROM 'library.csv' WITH DELIMITER ',' CSV;

-- Insert unique album titles into the album table
INSERT INTO album (title)
SELECT DISTINCT album FROM track;

-- Update the album_id column in the track table
UPDATE track
SET album_id = (SELECT id FROM album WHERE album.title = track.album);

-- Insert unique artist names into the artist table
INSERT INTO artist (name)
SELECT DISTINCT artist FROM track;




-- Insert unique track_id and artist_id combinations into the tracktoartist table
INSERT INTO tracktoartist (track_id, artist_id)
SELECT t.id, a.id
FROM track t
JOIN artist a ON t.artist = a.name;

-- Update the track_id column in the tracktoartist table
UPDATE tracktoartist
SET track_id = t.id
FROM track t
WHERE tracktoartist.track = t.title;

-- Update the artist_id column in the tracktoartist table
UPDATE tracktoartist
SET artist_id = a.id
FROM artist a
WHERE tracktoartist.artist = a.name;

-- We are now done with these text fields
ALTER TABLE track DROP COLUMN album;
ALTER TABLE track DROP COLUMN artist;

ALTER TABLE tracktoartist DROP COLUMN track;
ALTER TABLE tracktoartist DROP COLUMN artist;

-- Retrieve data from the tables and limit the result to 3 rows
SELECT track.title, album.title, artist.name
FROM track
JOIN album ON track.album_id = album.id
JOIN tracktoartist ON track.id = tracktoartist.track_id
JOIN artist ON tracktoartist.artist_id = artist.id
LIMIT 3;
