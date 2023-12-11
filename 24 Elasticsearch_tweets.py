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

# Edit elastictweet.py and loop through the automatically generated tweets. 
# index them as documents in your Elasticsearch index with tweet text stored in the field text.
nano elastictweet.py

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
# set indexname equal to username
indexname = secrets['user']

# Start fresh
res = es.indices.delete(index=indexname, ignore=[400, 404])
print("Dropped index")
print(res)
res = es.indices.create(index=indexname)
print("Created the index...")
print(res)

tweet_texts = [
    "typographical error but not if the problem is a conceptual misunderstanding",
    "If you dont understand what your program does you can read it 100 times and never see the error because the error is in",
    "Running experiments can help especially if you run small simple tests",
    "But if you run experiments without thinking or reading your code you",
]
for tweet_text in tweet_texts:
    # Indexing a document
    doc = {
        'author': 'kimchy',
        'type' : 'tweet',
        'text': tweet_text,
        'timestamp': datetime.now(),
    }
    res = es.index(index=indexname, id='abc', body=doc)
    print('Added document...')
    print(res['result'])
    # Retrieving a document
    res = es.get(index=indexname, id='abc')
    print('Retrieved document...')
    print(res)
    # Refreshing the index
    res = es.indices.refresh(index=indexname)
    print("Index refreshed")
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

# Run Elasticsearch tweets
python3 elastictweet.py

# Outputs
Dropped index
{'acknowledged': True}
Created the index...
{'acknowledged': True, 'shards_acknowledged': True, 'index': 'pg4e_f2e8cb0f32'}
Added document...
created
Retrieved document...
{'_index': 'pg4e_f2e8cb0f32', '_type': '_doc', '_id': 'abc', '_version': 1, '_seq_no': 0, '_primary_term': 1, 'found': True, '_source': {'author': 'kimchy', 'type': 'tweet', 'text': 'typographical error but not if the problem is a conceptual misunderstanding', 'timestamp': '2023-12-11T18:09:11.812340'}}
Index refreshed
{'_shards': {'total': 2, 'successful': 1, 'failed': 0}}
Search results...
{'took': 1, 'timed_out': False, '_shards': {'total': 1, 'successful': 1, 'skipped': 0, 'failed': 0}, 'hits': {'total': {'value': 1, 'relation': 'eq'}, 'max_score': 3.1645029, 'hits': [{'_index': 'pg4e_f2e8cb0f32', '_type': '_doc', '_id': 'abc', '_score': 3.1645029, '_source': {'author': 'kimchy', 'type': 'tweet', 'text': 'typographical error but not if the problem is a conceptual misunderstanding', 'timestamp': '2023-12-11T18:09:11.812340'}}]}}

Got 1 Hits:
2023-12-11T18:09:11.812340 kimchy: typographical error but not if the problem is a conceptual misunderstanding
Added document...
updated
Retrieved document...
{'_index': 'pg4e_f2e8cb0f32', '_type': '_doc', '_id': 'abc', '_version': 2, '_seq_no': 1, '_primary_term': 1, 'found': True, '_source': {'author': 'kimchy', 'type': 'tweet', 'text': 'If you dont understand what your program does you can read it 100 times and never see the error because the error is in', 'timestamp': '2023-12-11T18:09:12.326846'}}
Index refreshed
{'_shards': {'total': 2, 'successful': 1, 'failed': 0}}
Search results...
{'took': 1, 'timed_out': False, '_shards': {'total': 1, 'successful': 1, 'skipped': 0, 'failed': 0}, 'hits': {'total': {'value': 1, 'relation': 'eq'}, 'max_score': 12.577807, 'hits': [{'_index': 'pg4e_f2e8cb0f32', '_type': '_doc', '_id': 'abc', '_score': 12.577807, '_source': {'author': 'kimchy', 'type': 'tweet', 'text': 'If you dont understand what your program does you can read it 100 times and never see the error because the error is in', 'timestamp': '2023-12-11T18:09:12.326846'}}]}}

Got 1 Hits:
2023-12-11T18:09:12.326846 kimchy: If you dont understand what your program does you can read it 100 times and never see the error because the error is in
Added document...
updated
Retrieved document...
{'_shards': {'total': 2, 'successful': 1, 'failed': 0}}
{'_index': 'pg4e_f2e8cb0f32', '_type': '_doc', '_id': 'abc', '_version': 3, '_seq_no': 2, '_primary_term': 1, 'found': True, '_source': {'au
thor': 'kimchy', 'type': 'tweet', 'text': 'Running experiments can help especially if you run small simple tests', 'timestamp': '2023-12-11T
18:09:12.753036'}}
Index refreshed
{'_shards': {'total': 2, 'successful': 1, 'failed': 0}}
Search results...
{'took': 1, 'timed_out': False, '_shards': {'total': 1, 'successful': 1, 'skipped': 0, 'failed': 0}, 'hits': {'total': {'value': 1, 'relatio
n': 'eq'}, 'max_score': 10.086273, 'hits': [{'_index': 'pg4e_f2e8cb0f32', '_type': '_doc', '_id': 'abc', '_score': 10.086273, '_source': {'a
uthor': 'kimchy', 'type': 'tweet', 'text': 'Running experiments can help especially if you run small simple tests', 'timestamp': '2023-12-11
T18:09:12.753036'}}]}}
Got 1 Hits:
2023-12-11T18:09:12.753036 kimchy: Running experiments can help especially if you run small simple tests
Added document...
updated
Retrieved document...
{'_index': 'pg4e_f2e8cb0f32', '_type': '_doc', '_id': 'abc', '_version': 4, '_seq_no': 3, '_primary_term': 1, 'found': True, '_source': {'au
thor': 'kimchy', 'type': 'tweet', 'text': 'But if you run experiments without thinking or reading your code you', 'timestamp': '2023-12-11T1
8:09:13.218929'}}
Index refreshed
{'_shards': {'total': 2, 'successful': 1, 'failed': 0}}
Search results...
{'took': 1, 'timed_out': False, '_shards': {'total': 1, 'successful': 1, 'skipped': 0, 'failed': 0}, 'hits': {'total': {'value': 1, 'relatio
n': 'eq'}, 'max_score': 10.60387, 'hits': [{'_index': 'pg4e_f2e8cb0f32', '_type': '_doc', '_id': 'abc', '_score': 10.60387, '_source': {'aut
hor': 'kimchy', 'type': 'tweet', 'text': 'But if you run experiments without thinking or reading your code you', 'timestamp': '2023-12-11T18
:09:13.218929'}}]}}
Got 1 Hits:
2023-12-11T18:09:13.218929 kimchy: But if you run experiments without thinking or reading your code you
