-- Create a table named bigtext with a single TEXT column named content. Insert 100000 records with numbers starting at 100000 and going through 199999 into the table as shown below:

/*
This is record number 100000 of quite a few text records.
This is record number 100001 of quite a few text records.
...
This is record number 199998 of quite a few text records.
This is record number 199999 of quite a few text records.
*/

CREATE TABLE bigtext (
    content TEXT
);

INSERT INTO bigtext (content)
SELECT 'This is record number ' || generate_series || ' of quite a few text records.'
FROM generate_series(100000, 199999);
