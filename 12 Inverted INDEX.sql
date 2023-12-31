CREATE TABLE docs01 (id SERIAL, doc TEXT, PRIMARY KEY(id));
CREATE TABLE

CREATE TABLE invert01 (
   keyword TEXT,
   doc_id INTEGER REFERENCES docs01(id) ON DELETE CASCADE
 );
CREATE TABLE
INSERT INTO docs01 (doc) VALUES
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

INSERT INTO invert01 (doc_id, keyword)
 SELECT DISTINCT id, keyword
 FROM docs01 AS D, unnest(string_to_array(lower(D.doc), ' ')) keyword;
INSERT 0 117
SELECT keyword, doc_id FROM invert01 ORDER BY keyword, doc_id LIMIT 10;
 keyword | doc_id 
---------+--------
 100     |      2
 a       |      5
 a       |      7
 a       |     10
 about   |      9
 an      |      8
 and     |      2
 are     |     10
 at      |      9
 because |      2
(10 rows)
