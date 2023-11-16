-- Drop existing tables if they exist
DROP TABLE IF EXISTS unesco, unesco_raw, category, iso, state, region;

-- Create the unesco_raw table to hold the raw data
CREATE TABLE unesco_raw (
  name TEXT,
  description TEXT,
  justification TEXT,
  year INTEGER,
  longitude FLOAT,
  latitude FLOAT,
  area_hectares FLOAT,
  category TEXT,
  category_id INTEGER,
  state TEXT,
  state_id INTEGER,
  region TEXT,
  region_id INTEGER,
  iso TEXT,
  iso_id INTEGER
);

-- Create the category table
CREATE TABLE category (
  id SERIAL,
  name VARCHAR(128) UNIQUE,
  PRIMARY KEY (id)
);

-- Create the iso table
CREATE TABLE iso (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE
);

-- Create the state table
CREATE TABLE state (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE
);

-- Create the region table
CREATE TABLE region (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE
);

-- Use \COPY to load data from a server-side file (Make sure the file is accessible)
\copy unesco_raw(name, description, justification, year, longitude, latitude, area_hectares, category, state, region, iso) FROM PROGRAM 'curl -s https://www.pg4e.com/tools/sql/whc-sites-2018-small.csv' WITH (FORMAT CSV, HEADER);

-- Insert unique category values into the category table
INSERT INTO category(name) SELECT DISTINCT category FROM unesco_raw;
INSERT INTO state(name) SELECT DISTINCT state FROM unesco_raw;
INSERT INTO region(name) SELECT DISTINCT region FROM unesco_raw;
INSERT INTO iso(name) SELECT DISTINCT iso FROM unesco_raw;

-- Populate foreign key columns in the unesco_raw table
UPDATE unesco_raw SET category_id = (
  SELECT category.id FROM category WHERE category.name = unesco_raw.category);
UPDATE unesco_raw SET state_id = ( 
  SELECT state.id FROM state WHERE state.name = unesco_raw.state );
UPDATE unesco_raw SET region_id = (
    SELECT region.id FROM region WHERE region.name = unesco_raw.region);
UPDATE unesco_raw SET iso_id = (
    SELECT iso.id FROM iso WHERE iso.name = unesco_raw.iso);

-- Create the unesco table with normalized data
CREATE TABLE unesco (
    name TEXT,
    description TEXT,
    justification TEXT,
    year INTEGER,
    longitude FLOAT,
    latitude FLOAT,
    area_hectares FLOAT,
    category_id INTEGER,
    state_id INTEGER,
    region_id INTEGER,
    iso_id INTEGER
);

-- Insert data into the unesco table from unesco_raw
INSERT INTO unesco (
  name,
  description,
  justification,
  year,
  longitude,
  latitude,
  area_hectares,
  category_id,
  state_id,
  region_id,
  iso_id
) SELECT
  name,
  description,
  justification,
  year,
  longitude,
  latitude,
  area_hectares,
  category_id,
  state_id,
  region_id,
  iso_id
FROM unesco_raw;

-- Retrieve data from the normalized unesco table
SELECT unesco.name, year, category.name, state.name, region.name, iso.name
FROM unesco
JOIN category ON unesco.category_id = category.id
JOIN iso ON unesco.iso_id = iso.id
JOIN state ON unesco.state_id = state.id
JOIN region ON unesco.region_id = region.id
ORDER BY state.name, unesco.name
LIMIT 3;
