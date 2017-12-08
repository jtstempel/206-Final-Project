## Joseph Stempel

## Import Statements

import facebook
import unittest
import json
import sqlite3
import requests
import Facebook_Info
from pprint import pprint

## import webbrowser
## import itertools
## import collections

my_app_id = Facebook_Info.my_app_id
my_app_secret = Facebook_Info.my_app_secret
my_access_token = Facebook_Info.my_access_token

my_graph = facebook.GraphAPI(access_token = my_access_token, version = '2.1')
posts_on_my_timeline = my_graph.request('/me/feed')
pprint (posts_on_my_timeline)


CACHE_FNAME = 'Stempel_Final_Project_Cache.json'

try:
	cache_file = open(CACHE_FNAME,'r')		
	cache_contents = cache_file.read()
	cache_file.close()
	CACHE_DICTION = json.loads(cache_contents)
except:
	CACHE_DICTION = {}


##def get_user_posts(my_user):

##	if my_user in CACHE_DICTION:
##		print ('Using Cache...')
##		my_info = CACHE_DICTION[my_user]
##		return my_info
##	else:
##		print ('Fetching data...')
##		my_info = ...
##		CACHE_DICTION[my_user] = my_info

##		writing_file = open(CACHE_DICTION, 'w')
##		writing_file.write(json.dumps(CACHE_DICTION))
##		writing_file.close()

##	return my_info








