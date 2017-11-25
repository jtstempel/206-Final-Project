import unittest
import json
import sqlite3


my_app_id = '2497254837080155'
my_app_secret = '53b9b633590e8bb438abb4b74bf5f153'

CACHE_FNAME = 'Stempel_Final_Project_Cache.json'

try:
    cache_file = open(CACHE_FNAME,'r')		
    cache_contents = cache_file.read()
    cache_file.close()
    CACHE_DICTION = json.loads(cache_contents)
except:
    CACHE_DICTION = {}