## Joseph Stempel

import facebook
import unittest
import json
import sqlite3
import requests
## from pprint import pprint

## import webbrowser
## import itertools
## import collections

my_app_id = '2497254837080155'
my_app_secret = '53b9b633590e8bb438abb4b74bf5f153'
my_access_token = 'EAAjfPXN6UFsBAB1wthsVg58esuEtrR5nZARGVmZCUSZCMdgEmIFA6W8IdYd4XGwp10XcSh68jqwGXVA83uE0jOW8rhHVl0cYn0HJfeolbYE3dWbdumifrNJbDY0eTPejMZBbqxZB05XsGkoRfRkxqYnLj1QhfF0yR6yWGG9JtK20LEhvQe7X8J3nc5ABktnD16laJDk3v9gZDZD'
## user_id = '1780949455269404'

my_graph = facebook.GraphAPI(access_token = my_access_token, version = '2.1')
posts_on_my_timeline = my_graph.request('/me/feed')
print (posts_on_my_timeline)




##CACHE_FNAME = 'Stempel_Final_Project_Cache.json'

##try:
##    cache_file = open(CACHE_FNAME,'r')		
##    cache_contents = cache_file.read()
##    cache_file.close()
##    CACHE_DICTION = json.loads(cache_contents)
##except:
##    CACHE_DICTION = {}


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








