-- The drop table, create table, and insert into may be skipped since we alredy have done it in the last assignment.
DROP TABLE docs03;
DROP TABLE

CREATE TABLE docs03 (id SERIAL, doc TEXT, PRIMARY KEY(id));
CREATE TABLE

INSERT INTO docs03 (doc) VALUES
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

-- Insert filler rows
INSERT INTO docs03 (doc) SELECT 'Neon ' || generate_series(10000,20000);
INSERT 0 10001


CREATE INDEX fulltext03 ON docs03 USING gin(to_tsvector('english', doc));
CREATE INDEX

SELECT id, doc FROM docs03 WHERE to_tsquery('english', 'misunderstanding') @@ to_tsvector('english', doc);
id |                                doc                                 
----+--------------------------------------------------------------------
  1 | misunderstanding If you dont understand what your program does you
(1 row)

EXPLAIN SELECT id, doc FROM docs03 WHERE to_tsquery('english', 'misunderstanding') @@ to_tsvector('english', doc);
  QUERY PLAN                                        
-----------------------------------------------------------------------------------------
 Bitmap Heap Scan on docs03  (cost=12.39..81.75 rows=50 width=36)
   Recheck Cond: ('''instruct'''::tsquery @@ to_tsvector('english'::regconfig, doc))
   ->  Bitmap Index Scan on fulltext03  (cost=0.00..12.38 rows=50 width=0)
         Index Cond: ('''instruct'''::tsquery @@ to_tsvector('english'::regconfig, doc))
(4 rows)
