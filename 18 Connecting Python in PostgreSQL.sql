-- Connecting Python to PostgreSQL

-- In psql, check out tables:
\dt

-- Clean up tables from previous assignments to prevent running out of space
DROP TABLE table CASCADE;

-- Ensure you have a database connector. Install psycopg2 if not already installed:
$ pip3 install psycopg2

-- Download the simple.py code (contains connection data)
$ wget https://www.pg4e.com/code/simple.py

-- Download the hidden-dist.py
$ wget https://www.pg4e.com/code/hidden-dist.py

-- Take a look at hidden-dist.py
$ vi hidden-dist.py

-- Copy hidden-dist.py to hidden.py, containing the actual data
$ cp hidden-dist.py hidden.py

-- Take a look at hidden.py
$ vi hidden.py

-- Copy hidden.py to the current directory
$ cp ../code/hidden.py .

-- List files in long format, one per line
$ ls -l

-- The results shown are:
hidden-dist.py
hidden.py
simple.py

-- Take a look at simple.py to understand the imported modules and connection setup
$ vi simple.py

-- Run python3 simple.py
$ python3 simple.py

-- When you run the command python simple.py in the terminal, it will execute the code in the simple.py script below:

-- Import necessary modules (psycopg2 and hidden)
import psycopg2
import hidden

-- Load database connection information from hidden.py using the hidden.secrets() function
secrets = hidden.secrets()  -- a dictionary containing database credentials

-- Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host=secrets['host'],
    port=secrets['port'],
    database=secrets['database'],
    user=secrets['user'],
    password=secrets['pass'],
    connect_timeout=3
)

-- Create a cursor, a crucial component when working with relational databases using Python
cur = conn.cursor()

-- Attempt to drop the table named pythonfun if it exists and print the corresponding SQL command
sql = 'DROP TABLE IF EXISTS pythonfun CASCADE;'
print(sql)
cur.execute(sql)  -- execute SQL command

-- Attempt to create a new table named pythonfun with columns id (auto-incremented serial) and line (text)
sql = 'CREATE TABLE pythonfun (id SERIAL, line TEXT);'
print(sql)
cur.execute(sql)  -- execute SQL command

-- Commit changes to the database
conn.commit()

-- Enter a loop to insert 10 records into the pythonfun table
for i in range(10):
    txt = "Have a nice day " + str(i)
    sql = 'INSERT INTO pythonfun (line) VALUES (%s);'
    cur.execute(sql, (txt,))

-- Commit these changes to the database
conn.commit()

-- Perform a SELECT query to retrieve the id and line of the record where id=5
sql = "SELECT id, line FROM pythonfun WHERE id=5;"
print(sql)
cur.execute(sql)

-- Fetch the result of the SELECT query
row = cur.fetchone()
if row is None:
    print('Row not found')
else:
    print('Found', row)

-- Insert another record into the pythonfun table with a line containing "Have a nice day 9"
-- Print the new id returned by the RETURNING clause
sql = 'INSERT INTO pythonfun (line) VALUES (%s) RETURNING id;'
cur.execute(sql, (txt,))
id = cur.fetchone()[0]  -- fetch the result, the id value
print('New id', id)

-- Note: Here should have a conn.commit() to send the changes to the DB

-- Intentionally make a mistake in the SQL query
sql = "SELECT line FROM pythonfun WHERE mistake=5;"
print(sql)
cur.execute(sql)  -- This will not execute because the previous INSERT INTO statement was not flushed into the DB (conn.commit())

-- Commit any pending changes to the database and close the cursor
conn.commit()
cur.close()
