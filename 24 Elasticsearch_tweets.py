# Load elasticyweet.py https://www.pg4e.com/code/elastictweet.py
wget https://www.pg4e.com/code/elastictweet.py

# Install 'elasticsearch<7.14.0'
pip install 'elasticsearch<7.14.0'

# Load  hidden-dist.py https://www.pg4e.com/code/hidden-dist.py
wget https://www.pg4e.com/code/hidden-dist.py

# copy hidden-dist.py to hidden.py
cp hidden-dist.py  hidden.py

# edit hidden.py and put in your credentials
nano hidden.py

# Import the necessary libraries
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import RequestsHttpConnection
import hidden

secrets = hidden.elastic()
es = Elasticsearch(
    [secrets['host']],
    http_auth=(secrets['user'], secrets['pass']),
    url_prefix = secrets['prefix'],
    scheme=secrets['scheme'],
    port=secrets['port'],
    connection_class=RequestsHttpConnection,
)
indexname = secrets['user']

# Start fresh
res = es.indices.delete(index=indexname, ignore=[400, 404])
print("Dropped index")
print(res)
res = es.indices.create(index=indexname)
print("Created the index...")
print(res)

# Loop through the automatically generated tweets above and index them as documents in your Elasticsearch index with tweet text stored in the field text.
tweet_texts = [
    "typographical error but not if the problem is a conceptual misunderstanding",
    "If you dont understand what your program does you can read it 100 times and never see the error because the error is in",
    "Running experiments can help especially if you run small simple tests",
    "But if you run experiments without thinking or reading your code you",
]
for tweet_text in tweet_texts:
    doc = {
        'author': 'kimchy',
        'type' : 'tweet',
        'text': tweet_text,
        'timestamp': datetime.now(),
    }
    res = es.index(index=indexname, id='abc', body=doc)
    print('Added document...')
    print(res['result'])
    res = es.get(index=indexname, id='abc')
    print('Retrieved document...')
    print(res)

# Read the documents with a search term
    x = {
      "query": {
        "bool": {
          "must": {
            "match": {
              "text": tweet_text
            }
          },
          "filter": {
            "match": {
              "type": "tweet" 
            }
          }
        }
      }
    }
    res = es.search(index=indexname, body=x)
    print('Search results...')
    print(res)
    print()
    print("Got %d Hits:" % len(res['hits']['hits']))
    for hit in res['hits']['hits']:
        s = hit['_source']
        print(f"{s['timestamp']} {s['author']}: {s['text']}")
