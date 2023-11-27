# Loading JSON from PokéAPI: retrieving data from the PokéAPI and store the resulting data in a database.

$ pip3 install psycopg2 
$ pip3 install hidden 
$ python3
import psycopg2
import hidden
import time
import myutils
import requests
import json

# load the secrets
secrets = hidden.secrets()  

conn = psycopg2.connect(host=secrets['host'],
        port=secrets['port'],
        database=secrets['database'],
        user=secrets['user'],
        password=secrets['pass'],
        connect_timeout=3)
# You can include a print statement to display the database connection parameters as following:
# print(f'Connected to database {secrets["database"]} on {secrets["host"]}:{secrets["port"]} as user {secrets["user"]}')

# Create a cursor object
cur = conn.cursor()

# Create the pokeapi table if not exists
defaulturl = 'https://pokeapi.co/api/v2/pokemon/1/'
print('If you want to restart the spider, run')
print('DROP TABLE IF EXISTS pokeapi CASCADE;')
print(' ')

sql = 'DROP TABLE IF EXISTS pokeapi CASCADE;'
print(sql)
cur.execute(sql) 

sql = 'CREATE TABLE IF NOT EXISTS pokeapi (id INTEGER, body JSONB);'
print(sql)
cur.execute(sql)

conn.commit()    

-- URL for the PokeAPI
base_url = 'https://pokeapi.co/api/v2/pokemon/'

--  load the first 100 Pokémon JSON documents from the PokéAPI and store them in a table
-- loop through the PokéAPI and retrieve the JSON data for urls ending in 1..100 and store it in the pokeapi table
-- loop through the numbers 1..100 and modify this URL (https://pokeapi.co/api/v2/pokemon/1) to retrieve the data for that item
for i in range(1, 101):
    url = f'{base_url}{i}/'
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        sql_insert = 'INSERT INTO pokeapi (id, body) VALUES (%s, %s);'
        cur.execute(sql_insert, (i, json.dumps(data)))
        print(f'Retrieved and stored data for item {i}')
    except requests.exceptions.RequestException as e:
        print(f'Error retrieving data for item {i}: {e}')
conn.commit()
cur.close()
