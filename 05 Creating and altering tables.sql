-- Creatinga new database

/* Connecting to PostgreSQL database

psql -h pg.pg4e.com -p 5432 -U pg4e_73285570e1 pg4e_73285570e1
*/

-- Creating the table pg4e_debug

CREATE TABLE pg4e_debug (
  id SERIAL,
  query VARCHAR(4096),
  result VARCHAR(4096),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY(id)
);

-- View the contents of this table 
SELECT query, result, created_at FROM pg4e_debug;

-- Creating the table pg4e_result

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

-- using ALTER TABLE
-- Add a column to your pg4e_debug table. The column can be any type you like - like INTEGER. neon289.

ALTER TABLE pg4e_debug ADD COLUMN neon289 INTEGER;

--View your data

SELECT neon289 FROM pg4e_debug LIMIT 1;

-- Using SELECT DISTINCT
/* Access details for a readonly database:

-- Connecting to readonly database

-- psql -h pg.pg4e.com -p 5432 -U readonly readonly*/

-- Check the schema for the taxdata table

/*
readonly=# \d+ taxdata
  Column  |          Type          |
----------+------------------------+
 id       | integer                |
 ein      | integer                |
 name     | character varying(255) |
 year     | integer                |
 revenue  | bigint                 |
 expenses | bigint                 |
 purpose  | text                   |
 ptid     | character varying(255) |
 ptname   | character varying(255) |
 city     | character varying(255) |
 state    | character varying(255) |
 url      | character varying(255) |
 */

-- Find the distinct values in the state column of the taxdata table in ascending order. Your query should only return these five rows
/* SELECT DISTINCT state FROM taxdata ORDER BY state ASC LIMIT 5;

AE
AK
AL
AP
AR
*/

