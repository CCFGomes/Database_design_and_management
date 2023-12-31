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

CREATE INDEX array03 ON docs03 USING gin(string_to_array(lower(doc), ' '));
CREATE INDEX

SELECT id, doc FROM docs03 WHERE '{misunderstanding}' <@ string_to_array(lower(doc), ' ');
 id |                                doc                                 
----+--------------------------------------------------------------------
  1 | misunderstanding If you dont understand what your program does you
(1 row)

EXPLAIN SELECT id, doc FROM docs03 WHERE '{misunderstanding}' <@ string_to_array(lower(doc), ' ');
                                          QUERY PLAN                                          
----------------------------------------------------------------------------------------------
 Bitmap Heap Scan on docs03  (cost=12.39..69.50 rows=50 width=36)
   Recheck Cond: ('{misunderstanding}'::text[] <@ string_to_array(lower(doc), ' '::text))
   ->  Bitmap Index Scan on array03  (cost=0.00..12.38 rows=50 width=0)
         Index Cond: ('{misunderstanding}'::text[] <@ string_to_array(lower(doc), ' '::text))
(4 rows)
