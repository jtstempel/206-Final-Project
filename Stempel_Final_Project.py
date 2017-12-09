## Joseph Stempel

## Import Statements

import facebook
import json
import sqlite3
import requests
import Facebook_Info
import datetime
from pprint import pprint
	
CACHE_FNAME = 'Stempel_Final_Project_Cache.json'

try:
	cache_file = open(CACHE_FNAME,'r')		
	cache_contents = cache_file.read()
	cache_file.close()
	CACHE_DICTION = json.loads(cache_contents)
except:
	CACHE_DICTION = {}

def getFacebookData(my_access_token):
	my_graph = facebook.GraphAPI(access_token = my_access_token, version = '2.1')
	posts_on_my_timeline = my_graph.request('/me/?fields=id,name,feed.limit(100){created_time,likes.limit(300),comments.limit(100),shares}')
	
	my_user_id = posts_on_my_timeline['id']

	if my_user_id in CACHE_DICTION:
		print ('Using Cache...')
		my_cached_data = CACHE_DICTION[my_user_id]

	else:
		print ('Fetching data...')

		my_list_of_posts = posts_on_my_timeline['feed']['data']
		number_of_posts = 0
		for post in my_list_of_posts:
			number_of_posts += 1

		## print (number_of_posts)

		list_of_post_ids = []
		for post in my_list_of_posts:
			list_of_post_ids.append(post['id'])

		list_of_number_of_likers = []
		for each_post in my_list_of_posts:
			number_of_likers = 0
			if 'likes' in each_post.keys():
				for liker in each_post['likes']['data']:
					number_of_likers += 1
			list_of_number_of_likers.append(number_of_likers)

		## print (list_of_number_of_likers)

		list_of_number_of_comments = []
		for a_post in my_list_of_posts:
			number_of_commenters = 0
			if 'comments' in a_post.keys():
				for commenter in a_post['comments']['data']:
					number_of_commenters += 1
			list_of_number_of_comments.append(number_of_commenters)


		list_of_weekdays = []

		for my_post in my_list_of_posts:

			post_year = my_post['created_time'][:4]
			post_month = my_post['created_time'][5:7]
			post_day = my_post['created_time'][8:10]

			my_tuple = (post_year, post_month, post_day)
			my_weekday = datetime.datetime(int(post_year), int(post_month), int(post_day))
			day_of_the_week = my_weekday.weekday()

			if day_of_the_week == 6:
				my_day = 'Sunday'

			elif day_of_the_week == 0:
				my_day = 'Monday'

			elif day_of_the_week == 1:
				my_day = 'Tuesday'

			elif day_of_the_week == 2:
				my_day = 'Wednesday'

			elif day_of_the_week == 3:
				my_day = 'Thursday'

			elif day_of_the_week == 4:
				my_day = 'Friday'

			elif day_of_the_week == 5:
				my_day = 'Saturday'

			list_of_weekdays.append(my_day)


		complete_dictionary = {}
		for x in range(len(list_of_post_ids)):
			complete_dictionary[list_of_post_ids[x]] = (list_of_weekdays[x], list_of_number_of_likers[x], list_of_number_of_comments[x])

	
		CACHE_DICTION[my_user_id] = complete_dictionary
		my_cached_data = complete_dictionary

		writing_file = open(CACHE_FNAME, 'w')
		writing_file.write(json.dumps(CACHE_DICTION))
		writing_file.close()

	return my_cached_data

pprint (getFacebookData(Facebook_Info.my_access_token))

## SQL Setup

my_database = sqlite3.connect('facebook_posts.db')
cur = my_database.cursor()

cur.execute('DROP TABLE IF EXISTS Facebook_Posts')
cur.execute('CREATE TABLE Facebook_Posts (post_id TEXT, weekday_posted TEXT, number_of_likers NUMBER, number_of_comments NUMBER)')

facebook_posts = getFacebookData(Facebook_Info.my_access_token)

for my_var in facebook_posts.keys():
	my_tup = str(my_var), str(facebook_posts[my_var][0]), int(facebook_posts[my_var][1]), int(facebook_posts[my_var][2])
	cur.execute('INSERT INTO Facebook_Posts (post_id, weekday_posted, number_of_likers, number_of_comments) VALUES (?, ?, ?, ?)', my_tup)

my_database.commit()

cur.close()
my_database.close()
