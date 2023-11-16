--Musical tracks many-to-one

-- Create the 'album' table

CREATE TABLE album (
  id SERIAL,
  title VARCHAR(128) UNIQUE,
  PRIMARY KEY(id)
);

-- Create the 'track' table with a foreign key reference to 'album'

CREATE TABLE track (
    id SERIAL,
    title VARCHAR(128),
    len INTEGER, rating INTEGER, count INTEGER,
    album_id INTEGER REFERENCES album(id) ON DELETE CASCADE,
    UNIQUE(title, album_id),
    PRIMARY KEY(id)
);

-- Drop the 'track_raw' table if it exists

DROP TABLE IF EXISTS track_raw;

-- Create the 'track_raw' table to hold raw data

CREATE TABLE track_raw
 (title TEXT, artist TEXT, album TEXT, album_id INTEGER,
  count INTEGER, rating INTEGER, len INTEGER);

-- copy https://www.pg4e.com/tools/sql/library.csv?PHPSESSID=63c5f0c79e884dad9c14aabdeb15cb23%22

-- Update 'album_id' in 'track_raw' based on matching album titles

UPDATE track_raw SET album_id = (SELECT album.id FROM album WHERE album.title = track_raw.album);

-- Load data from 'library.csv' into 'track_raw' table
\copy track_raw(title, artist, album, album_id, count, rating, len) FROM 'library.csv' DELIMITER ',' CSV HEADER;

-- Insert distinct albums into the 'album' table

INSERT INTO album (title)
SELECT DISTINCT album FROM track_raw;

-- Update 'album_id' in 'track_raw' based on matching album titles again

UPDATE track_raw SET album_id = (SELECT album.id FROM album WHERE album.title = track_raw.album);

-- Copy data from 'track_raw' to 'track' while dropping artist and album text fields

INSERT INTO track (title, len, rating, count, album_id)
SELECT title, len, rating, count, album_id FROM track_raw;

-- Query to verify the results 

SELECT track.title, album.title
FROM track
JOIN album ON track.album_id = album.id
ORDER BY track.title
LIMIT 3;

           title            |               title                
----------------------------+------------------------------------
 A Boy Named Sue (live)     | The Legend Of Johnny Cash
 A Brief History of Packets | Computing Conversations
 Aguas De Marco             | Natural Wonders Music Sampler 1999
(3 rows)






