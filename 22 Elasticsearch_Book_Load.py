# download a book from: https://www.pg4e.com/gutenberg/cache/epub/14091/pg14091.txt
wget https://www.pg4e.com/gutenberg/cache/epub/14091/pg14091.txt

# Load https://www.pg4e.com/code/elasticbook.py
wget https://www.pg4e.com/code/elasticbook.py

# Load  https://www.pg4e.com/code/elastictool.py
wget  https://www.pg4e.com/code/elastictool.py

# Load https://www.pg4e.com/code/hidden-dist.py
wget https://www.pg4e.com/code/hidden-dist.py

# copy hidden-dist.py to hidden.py and edit the credentials with yours
cp hidden-dist.py hidden.py
nano hidden.py

# instal 'elasticsearch<7.14.0'
pip install 'elasticsearch<7.14.0'

python3 elasticbook.py
enter book file: pg14091.txt

Enter book file (i.e. pg18866.txt): pg14091.txt
Dropped index pg4e_f2e8cb0f32
{'acknowledged': True}
Created the index...
{'acknowledged': True, 'shards_acknowledged': True, 'index': 'pg4e_f2e8cb0f32'}
Added document 2c736a512bac087e60fefc8b9eb11889b044d6a200a53b72b8bc239189f56a50
...
Added document 4b119a0cb219a1426a699d593cbdbf79439a7c317037b583b67326f26a0a5d4a
Index refreshed pg4e_f2e8cb0f32
{'_shards': {'total': 2, 'successful': 1, 'failed': 0}}
 
Loaded 2658 paragraphs 17696 lines 875237 characters

python3 elastictool.py
Enter command: search repose
https://pg4e_f2e8cb0f32:*****@www.pg4e.com:443/elasticsearch/pg4e_f2e8cb0f32/_search?pretty
{"query": {"query_string": {"query": "repose"}}}
200
{
  "took": 16,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 2,
      "relation": "eq"
    },
    "max_score": 10.892093,
    "hits": [
      {
        "_index": "pg4e_f2e8cb0f32",
        "_type": "_doc",
        "_id": "4ba2b3a5396a4af993832f0fca5cbea2838e5b62aa2f492739b11513839d6304",
        "_score": 10.892093,
        "_source": {
          "offset": 2597,
          "content": " CONSUMPTION OF AIR IN ACTIVITY AND REPOSE."
        }
      },
      {
        "_index": "pg4e_f2e8cb0f32",
        "_type": "_doc",
        "_id": "f6dfb329dc8ee816e11755ce5025f1cccb175d15540852590ec166c1d6870e80",
        "_score": 6.148485,
        "_source": {
          "offset": 2598,
          "content": " Dr. Radclyffe Hall makes the following interesting statement with regard to the amount of air we consume in repose, and at dif
ferent degrees of activity: When still, we use 500 cubic inches of air in a minute; if we walk at the rate of one mile an hour, we use 800; two miles
, 1,000; three miles an hour, 1,600; four miles an hour, 2,300. If we run at six miles an hour, we use 3,000 cubic inches; trotting a horse, 1,750; c
antering, 1,500."
        }
      }
    ]
  }
}
Enter command: quit

