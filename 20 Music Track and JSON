-- Drop the table if it exists to avoid conflicts
DROP TABLE IF EXISTS jtrack CASCADE;

-- Create the jtrack table with id as SERIAL and body as JSONB
CREATE TABLE IF NOT EXISTS jtrack (id SERIAL, body JSONB);

-- Import JSON data using the COPY command from 'library.jstxt'
-- The data is in CSV format with non-printable characters as delimiters and quotes
-- Source: https://www.pg4e.com/code/library.jstxt
\copy jtrack (body) FROM 'library.jstxt' WITH CSV QUOTE E'\x01' DELIMITER E'\x02'; 

-- QUOTE E'\x01: This option sets the quoting character for CSV. In this case, it's set to a non-printable character represented as a hexadecimal escape sequence (\x01). 
-- This is used to ensure that the quoting character won't conflict with the data.
-- DELIMITER E'\x02: This option sets the delimiter for CSV. Similar to the quoting character, it's set to a non-printable character represented as a hexadecimal escape sequence (\x02). 
-- This delimiter is used to separate values in the CSV file.
-- Both are used to help avoid conflicts with the actual data in the CSV file.

-- Display the first 5 rows of the jtrack table
SELECT * FROM jtrack LIMIT 5;

-- Display the data type of the 'body' column in the first row
SELECT pg_typeof(body) FROM jtrack LIMIT 1;

-- Extract the 'name' field from the 'body' column for the first 5 rows
SELECT body->>'name' FROM jtrack LIMIT 5;

-- Demonstrate different ways to check the data type of 'body->'name''
SELECT pg_typeof(body->'name') FROM jtrack LIMIT 1;
SELECT pg_typeof(body->'name'::text) FROM jtrack LIMIT 1;
SELECT pg_typeof(body->'name')::text FROM jtrack LIMIT 1;
SELECT pg_typeof((body->'name')::text) FROM jtrack LIMIT 1;

-- Use the most straightforward way to check the data type
SELECT pg_typeof(body->>'name') FROM jtrack LIMIT 1;

-- Find the maximum value of 'count' in the JSONB data
SELECT MAX((body->>'count')::int) FROM jtrack;

-- Display the 'name' and 'count' ordered by count in descending order for the first 5 rows
SELECT body->>'name' AS name FROM jtrack ORDER BY (body->>'count')::int DESC LIMIT 5;

-- Demonstrate the need for casting when working with integer values in JSON
SELECT pg_typeof(body->'count') FROM jtrack LIMIT 1;
SELECT pg_typeof(body->>'count') FROM jtrack LIMIT 1;

-- Check if a specific 'name' value exists in the JSONB data
SELECT COUNT(*) FROM jtrack WHERE body->>'name' = 'Summer Nights';

-- Check if the JSONB data contains a specific key-value pair for 'name'
SELECT COUNT(*) FROM jtrack WHERE body @> '{"name": "Summer Nights"}';
SELECT COUNT(*) FROM jtrack WHERE body @> ('{"name": "Summer Nights"}'::jsonb);

-- Add a new key-value pair to the JSONB column for entries with count greater than 200
UPDATE jtrack SET body = body || '{"favorite": "yes"}' WHERE (body->'count')::int > 200;

-- Display some rows with and without the "favorite" key
SELECT body FROM jtrack WHERE (body->'count')::int > 160 LIMIT 5;

-- Check if the 'favorite' key is present in the JSONB data
SELECT COUNT(*) FROM jtrack WHERE body ? 'favorite';

-- Insert bulk data into the table using a SELECT statement
INSERT INTO jtrack (body) 
SELECT ('{ "type": "Neon", "series": "24 Hours of Lemons", "number": ' || generate_series(1000,5000) || '}')::jsonb;

-- Drop existing indexes if they exist
DROP INDEX IF EXISTS jtrack_btree;
DROP INDEX IF EXISTS jtrack_gin;
DROP INDEX IF EXISTS jtrack_gin_path_ops;

-- Create indexes on the 'name' field, the entire 'body', and 'body' with jsonb_path_ops
CREATE INDEX jtrack_btree ON jtrack USING BTREE ((body->>'name'));
CREATE INDEX jtrack_gin ON jtrack USING gin (body);
CREATE INDEX jtrack_gin_path_ops ON jtrack USING gin (body jsonb_path_ops);

-- Wait for PostgreSQL to catch up, then explain which index each query uses
EXPLAIN SELECT COUNT(*) FROM jtrack WHERE body->>'artist' = 'Queen';
EXPLAIN SELECT COUNT(*) FROM jtrack WHERE body->>'name' = 'Summer Nights';
EXPLAIN SELECT COUNT(*) FROM jtrack WHERE body ? 'favorite';
EXPLAIN SELECT COUNT(*) FROM jtrack WHERE body @> '{"name": "Summer Nights"}';
EXPLAIN SELECT COUNT(*) FROM jtrack WHERE body @> '{"artist": "Queen"}';
EXPLAIN SELECT COUNT(*) FROM jtrack WHERE body @> '{"name": "Folsom Prison Blues", "artist": "Johnny Cash"}';

-- Demonstrate updating a numeric field in JSONB
-- First, attempt and fail, then succeed
SELECT (body->'count') + 1 FROM jtrack LIMIT 1;  -- it gives an error because I have given a JSONB and an integer, and it's not allowed to add them together. 
SELECT (body->'count')::int + 1 FROM jtrack LIMIT 1; -- Here we cast the body->'count' to an integer, so it works.

-- Update the 'count' field for entries with 'name' equal to 'Summer Nights'
UPDATE jtrack SET body = jsonb_set(body, '{ count }', ( (body->>'count')::int + 1 )::text::jsonb )
WHERE body->>'name' = 'Summer Nights';

-- Drop the table to avoid data and index space issues
DROP TABLE IF EXISTS jtrack CASCADE;
