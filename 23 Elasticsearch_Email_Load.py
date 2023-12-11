# Instal elasticsearch<7.14.0
pip install 'elasticsearch<7.14.0'

# load https://www.pg4e.com/code/hidden-dist.py
wget https://www.pg4e.com/code/hidden-dist.py

# copy hidden-dist.py to hidden.py (if necessary)
cp hidden-dist.py hidden.py

# edit hidden.py and put in your credentials
nano hidden.py

# load https://www.pg4e.com/code/datecompat.py
wget https://www.pg4e.com/code/datecompat.py

# load https://www.pg4e.com/code/elasticmail.py
wget https://www.pg4e.com/code/elasticmail.py

# load http://mbox.dr-chuck.net/sakai.devel/100/101
wget http://mbox.dr-chuck.net/sakai.devel/100/101

# enter python3 elasticmail.py and answer How many messages:
python3 elasticmail.py
How many messages:213

# enter python3 elastictool.py and Enter command: match_all
python3 elastictool.py
Enter command: match_all
https://pg4e_f2e8cb0f32:*****@www.pg4e.com:443/elasticsearch/pg4e_f2e8cb0f32/_search
200

# enter command search nebraska
Enter command: search nebraska

