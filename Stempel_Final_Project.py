## Joseph Stempel

## import statements?

import unittest
import json
import sqlite3
import webbrowser
from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import facebook_compliance_fix


## Facebook API

my_app_id = '2497254837080155'
my_app_secret = '53b9b633590e8bb438abb4b74bf5f153'

## Caching Setup

CACHE_FNAME = 'Stempel_Final_Project_Cache.json'

try:
    cache_file = open(CACHE_FNAME,'r')		
    cache_contents = cache_file.read()
    cache_file.close()
    CACHE_DICTION = json.loads(cache_contents)
except:
    CACHE_DICTION = {}

def myFacebookAuthorization():
	pass

def getUserPosts(my_user):
	if my_user in CACHE_DICTION:
		print ('Using Cache...')
		my_info = CACHE_DICTION[my_user]
		return my_info
	else:
		print ('Fetching data...')
		my_info = ...


## Access exactly 100 interactions

## Find the days that each of these interactions took place (find respective dates and times of posts)

## Find content of each post

## Find number of likes, number of shares?

## Potentially find comments on posts

## Write the data to a database

## Create a report