-- Entering Many-to-One Data - Automobiles

-- Create tables make and model

CREATE TABLE make (
    id SERIAL,
    name VARCHAR(128) UNIQUE,
    PRIMARY KEY(id)
);

CREATE TABLE model (
  id SERIAL,
  name VARCHAR(128),
  make_id INTEGER REFERENCES make(id) ON DELETE CASCADE,
  PRIMARY KEY(id)
);

-- Insert data into the tables make and model

INSERT INTO (make, model) VALUES('Hyundai','Excel');
INSERT INTO (make, model) VALUES ('Hyundai', 'Genesis');
INSERT INTO (make, model) VALUES ('Volkswagen', 'Tiguan 4motion');
INSERT INTO (make, model) VALUES('Hyundai','Equus');
INSERT INTO (make, model) VALUES('Hyundai','Excel');
INSERT INTO (make, model) VALUES ('Hyundai', 'Genesis');
INSERT INTO (make, model) VALUES ('Volkswagen', 'Tiguan 4motion');

-- Building a many-to-many roster
-- Create the tables student, course and the junction table roster

CREATE TABLE student (
    id SERIAL,
    name VARCHAR(128) UNIQUE,
    PRIMARY KEY(id)
);

DROP TABLE course CASCADE;
CREATE TABLE course (
    id SERIAL,
    title VARCHAR(128) UNIQUE,
    PRIMARY KEY(id)
);

DROP TABLE roster CASCADE;
CREATE TABLE roster (
    id SERIAL,
    student_id INTEGER REFERENCES student(id) ON DELETE CASCADE,
    course_id INTEGER REFERENCES course(id) ON DELETE CASCADE,
    role INTEGER,
    UNIQUE(student_id, course_id),
    PRIMARY KEY (id)
);


--  list all tables in the current schema

\dt
               List of relations
 Schema |    Name     | Type  |      Owner      
--------+-------------+-------+-----------------
 public | ages        | table | pg4e_73285570e1
 public | album       | table | pg4e_73285570e1
 public | automagic   | table | pg4e_73285570e1
 public | course      | table | pg4e_73285570e1
 public | make        | table | pg4e_73285570e1
 public | model       | table | pg4e_73285570e1
 public | pg4e_debug  | table | pg4e_73285570e1
 public | pg4e_meta   | table | pg4e_73285570e1
 public | pg4e_result | table | pg4e_73285570e1
 public | roster      | table | pg4e_73285570e1
 public | student     | table | pg4e_73285570e1
 public | track       | table | pg4e_73285570e1
 public | track_raw   | table | pg4e_73285570e1
 
(13 rows)
