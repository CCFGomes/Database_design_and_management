-- Creating the database

-- Initial Database Setup

-- Creating the table pg4e_debug

CREATE TABLE pg4e_debug (
  id SERIAL,
  query VARCHAR(4096),
  result VARCHAR(4096),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY(id)
);

-- Inserting data into the pg4e_debug table
INSERT INTO pg4e_debug (query, result) VALUES
    ('SELECT id, query, result, created_at FROM pg4e_debug', 'Success'),
    ('SELECT id, keystr, valstr FROM pg4e_meta', 'Success'),
    ('SELECT track.title, album.title FROM track JOIN album ON track.album_id = album.id ORDER BY track.title LIMIT 3', 'Success');

-- Retrieving it's content

SELECT query, result, created_at FROM pg4e_debug;
query                         | result  |         created_at         
------------------------------------------------------+---------+----------------------------
 SELECT id, query, result, created_at FROM pg4e_debug | Success | 2023-10-04 23:52:32.767675
 SELECT id, keystr, valstr FROM pg4e_meta             | Success | 2023-10-04 23:52:32.775473
 SELECT track.title, album.title                     +| Success | 2023-10-04 23:52:32.791638
     FROM track                                      +|         | 
     JOIN album ON track.album_id = album.id         +|         | 
     ORDER BY track.title LIMIT 3;                    |         | 
(3 rows)
-- 
CREATE TABLE pg4e_result (
  id SERIAL,
  link_id INTEGER UNIQUE,
  score FLOAT,
  title VARCHAR(4096),
  note VARCHAR(4096),
  debug_log VARCHAR(8192),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP
);

# Inserting some data

-- Create the table ages

CREATE TABLE ages ( 
  name VARCHAR(128), 
  age INTEGER
);

-- Make sure the table is empty by deleting any rows that you previously inserted, then insert values

DELETE FROM ages;
INSERT INTO ages (name, age) VALUES ('Cody', 34);
INSERT INTO ages (name, age) VALUES ('Darla', 35);
INSERT INTO ages (name, age) VALUES ('Franko', 38);
INSERT INTO ages (name, age) VALUES ('Saman', 31);
INSERT INTO ages (name, age) VALUES ('Toluwani', 15);









