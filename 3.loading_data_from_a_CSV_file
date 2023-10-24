-- Musical Track Database

-- Download this file https://www.pg4e.com/tools/sql/library.csv into the folder on system where you are running your psql client

--Create table track_raw

CREATE TABLE track_raw
 (title TEXT, artist TEXT, album TEXT,
  count INTEGER, rating INTEGER, len INTEGER);

--  Load it into the track_raw table using the psql \copy command.

\copy track_raw(title,artist,album,count,rating,len) FROM 'library.csv' WITH DELIMITER ',' CSV;

-- View the data

SELECT title, album FROM track_raw ORDER BY title LIMIT 3;
          title            |           album           
----------------------------+---------------------------
 A Boy Named Sue (live)     | The Legend Of Johnny Cash
 A Boy Named Sue (live)     | The Legend Of Johnny Cash
 A Brief History of Packets | Computing Conversations
(3 rows)
