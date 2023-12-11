# loadbook.py

# Download the Book:
# Use wget to download the book from Project Gutenberg: pg19337.txt.
wget http://www.gutenberg.org/cache/epub/19337/pg19337.txt

# Download necessary Python scripts:
# loadbook.py: Main script for loading the book into the database.
wget https://www.pg4e.com/code/loadbook.py 

# myutils.py: Library code used by loadbook.py.
wget https://www.pg4e.com/code/myutils.py

# hidden-dist.py: Template for storing database credentials.
wget https://www.pg4e.com/code/hidden-dist.py

# Set Up Database Credentials:
# Copy hidden-dist.py to hidden.py.
cp hidden-dist.py hidden.py
# Edit hidden.py and input your PostgreSQL credentials.
nano hidden.py

# Import necessary libraries
import psycopg2
import hidden
import time

# Get the book file input from the user
bookfile = input("Enter book file (i.e., pg19337.txt): ")
if bookfile == '':
    bookfile = 'pg19337.txt'

# Extract base name from the book file
base = bookfile.split('.')[0]

# Open the book file
fhand = open(bookfile)

# Connect to the PostgreSQL database
secrets = hidden.secrets()
conn = psycopg2.connect(
    host=secrets['host'],
    port=secrets['port'],
    database=secrets['database'],
    user=secrets['user'],
    password=secrets['pass'],
    connect_timeout=3
)
cur = conn.cursor()

# Drop existing table and create a new one
sql = 'DROP TABLE IF EXISTS ' + base + ' CASCADE;'
cur.execute(sql)

sql = 'CREATE TABLE ' + base + ' (id SERIAL, body TEXT);'
cur.execute(sql)

# Process paragraphs and insert into the database
# Commit every 50 records to improve performance
# Print loading updates every 100 records
# After completion, suggest creating a GIN index manually

# Commit remaining records and close the cursor
conn.commit()
cur.close()

# Print loading statistics
print(' ')
print('Loaded', pcount, 'paragraphs', count, 'lines', chars, 'characters')

# Suggest creating a GIN index manually
sql = 'CREATE INDEX ' + base + '_gin ON ' + base + ' USING gin(to_tsvector('english', body));'
print(' ')
print('Run this manually to make your index:')
print(sql)
