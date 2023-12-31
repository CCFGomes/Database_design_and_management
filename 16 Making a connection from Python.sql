# Download simple.py and hidden-dist.py, and rename hidden-dist.py to hidden.py:

wget https://www.pg4e.com/code/simple.py
wget https://www.pg4e.com/code/hidden-dist.py
mv hidden-dist.py hidden.py

# Edit hidden.py

nano hidden.py

# Inside hidden.py, replace the placeholder password with your actual password.

# Then, install psycopg2 library

pip3 install psycopg2

# Run simple.py

python3 simple.py

'''
DROP TABLE IF EXISTS pythonfun CASCADE;
CREATE TABLE pythonfun (id SERIAL, line TEXT);
SELECT id, line FROM pythonfun WHERE id=5;
Found (5, 'Have a nice day 4')
New id 11
SELECT line FROM pythonfun WHERE mistake=5;
Traceback (most recent call last):
  File "simple.py", line 66, in <module>
    cur.execute(sql)
psycopg2.errors.UndefinedColumn: column "mistake" does not exist
LINE 1: SELECT line FROM pythonfun WHERE mistake=5;
'''

# Check that the records are in the table by using psql and running:

SELECT line FROM pythonfun WHERE line LIKE 'Have a nice%';
     line        
-------------------
 Have a nice day 0
 Have a nice day 1
 Have a nice day 2
 Have a nice day 3
 Have a nice day 4
 Have a nice day 5
 Have a nice day 6
 Have a nice day 7
 Have a nice day 8
 Have a nice day 9
(10 rows)

