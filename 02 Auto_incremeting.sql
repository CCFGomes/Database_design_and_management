-- Serial fields / Auto Increment

/* 
Create a table named automagic with the following fields:
An id field that is an auto incrementing serial field.
A name field that allows up to 32 characters but no more This field is required. (PostgreSQL Constraints)
A height field that is a floating point number that is required. 
*/


CREATE TABLE automagic (
    id SERIAL PRIMARY KEY,
    name VARCHAR(32) NOT NULL,
    height FLOAT NOT NULL
);




/*
The id column is defined as a "SERIAL" data type. This means that, for each new row added to the automagic table, 
PostgreSQL will automatically assign a unique integer value to the id column.  It's an auto-incrementing serial field that serves as the primary key.

The PRIMARY KEY constraint designates this column as the primary key, ensuring its uniqueness and facilitating efficient indexing for retrieval operations.

The NOT NULL constraints require that a value be provided for these columns when inserting data into the tables. 
It ensures that the fields are mandatory and cannot be left empty.

This table is suitable for storing information about entities with names and heights, 
and it ensures that each entry has a unique identifier (the id) and that both the name and height are provided for each entry.
*/
