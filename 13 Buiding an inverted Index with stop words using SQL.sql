-- Create a table, and the inverted index; Then, insert into the table values
CREATE TABLE docs02 (id SERIAL, doc TEXT, PRIMARY KEY(id));
CREATE TABLE

CREATE TABLE invert02 (
   keyword TEXT,
   doc_id INTEGER REFERENCES docs02(id) ON DELETE CASCADE
 );
CREATE TABLE
INSERT INTO docs02 (doc) VALUES
 ('misunderstanding If you dont understand what your program does you'),
 ('can read it 100 times and never see the error because the error is in'),
 ('Running experiments can help especially if you run small simple tests'),
 ('But if you run experiments without thinking or reading your code you'),
 ('might fall into a pattern I call random walk programming which is the'),
 ('process of making random changes until the program does the right thing'),
 ('Needless to say random walk programming can take a long time'),
 ('You have to take time to think Debugging is like an experimental'),
 ('science You should have at least one hypothesis about what the problem'),
 ('is If there are two or more possibilities try to think of a test that');
INSERT 0 10

-- Create a stop_words table and insert into it values
CREATE TABLE stop_words (word TEXT unique);
CREATE TABLE

INSERT INTO stop_words (word) VALUES 
 ('i'), ('a'), ('about'), ('an'), ('are'), ('as'), ('at'), ('be'), 
 ('by'), ('com'), ('for'), ('from'), ('how'), ('in'), ('is'), ('it'), ('of'), 
 ('on'), ('or'), ('that'), ('the'), ('this'), ('to'), ('was'), ('what'), 
 ('when'), ('where'), ('who'), ('will'), ('with');
INSERT 0 30
INSERT INTO invert02 (doc_id, keyword)
 SELECT DISTINCT id, keyword
 FROM docs02 AS D, unnest(string_to_array(lower(D.doc), ' ')) keyword
 WHERE keyword NOT IN (SELECT word FROM stop_words)
 ORDER BY id;
INSERT 0 89

-- Retrieve the first 10 rows of the inverted index
SELECT keyword, doc_id FROM invert02 ORDER BY keyword, doc_id LIMIT 10;
 keyword | doc_id 
---------+--------
 100     |      2
 and     |      2
 because |      2
 but     |      4
 call    |      5
 can     |      2
 can     |      3
 can     |      7
 changes |      6
 code    |      4
(10 rows)
