## Joseph Stempel

## Import Statements

import facebook
import json
import sqlite3
import requests
import Facebook_Info
import datetime
from pprint import pprint			## Organizes output - makes it "pretty"
	
CACHE_FNAME = 'Final_Project_Cache.json'	## I am naming my cache file and saving it to variable CACHE_FNAME

try:
	cache_file = open(CACHE_FNAME,'r')				## Opening cache file	
	cache_contents = cache_file.read()			## Reading the data of this cache file into a string
	CACHE_DICTION = json.loads(cache_contents)		## Loading cache file data into python object
	cache_file.close()							## Closing cache file
except:
	CACHE_DICTION = {}					## If actions above do not run then I want the data to go to this dictionary CACHE_DICTION

def getFacebookData(my_access_token):
	my_graph = facebook.GraphAPI(access_token = my_access_token, version = '2.1')			## Accessing Facebook Graph API 
	posts_on_my_timeline = my_graph.request('/me/?fields=id,name,feed.limit(100){created_time,likes.limit(300),comments.limit(100)}')	## Making request for specific data fields of 100 posts (created_time, likes, comments) from Facebook Graph API, also setting appropriate limits to see all data  
	
	my_user_id = posts_on_my_timeline['id']

	if my_user_id in CACHE_DICTION:
		print ('\n')						## Adding unnecessary spacing so it looks nicer
		print ('Using Cache...')						
		print ('\n')
		my_cached_data = CACHE_DICTION[my_user_id]
		pprint(my_cached_data)				## Output
		return my_cached_data						## If data related to specific user_id is already in cache, return data

	else:											## If data related to specific user_id is not already in cache, run the following code to fetch data
		print ('\n')
		print ('Fetching data...')
		print ('\n')

		my_list_of_posts = posts_on_my_timeline['feed']['data']		## Making list of posts on user's personal feed (otherwise known as wall), indexing into appropriate nested data point to access these 100 posts
		number_of_posts = 0
		for post in my_list_of_posts:					## Incrementing or counting each post to ensure exactly 100 posts were grabbed
			number_of_posts += 1

		## print (number_of_posts)

		list_of_post_ids = []			## Initializing empty list
		for post in my_list_of_posts:
			list_of_post_ids.append(post['id'])		## Appending the ID of each post to empty list

		list_of_number_of_likers = []			## Initializing larger (empty) list that will contain the number of likers for each post
		for each_post in my_list_of_posts:
			number_of_likers = 0						## Initializing incrementer/counter
			if 'likes' in each_post.keys():						## Some posts do not receive any likes, so I am checking if a 'likes' field/data point exists in each post
				for liker in each_post['likes']['data']:			## If 'likes' exists in a post, add each liker to number_of_likers count
					number_of_likers += 1
			list_of_number_of_likers.append(number_of_likers)		## Appending the number of likers for each post to the larger list 

		## print (list_of_number_of_likers)

		list_of_number_of_comments = []				
		for a_post in my_list_of_posts:
			number_of_comments = 0
			if 'comments' in a_post.keys():							## Again, some posts do not receive any comments, so I am checking if a 'comments' field/data point exists in each post
				for commenter in a_post['comments']['data']:			## If it does exist, then count how many comments there are for each post
					number_of_comments += 1
			list_of_number_of_comments.append(number_of_comments)			## Appending the number of comments found for each individual post to the larger list containing the number of comments on all posts


		list_of_weekdays = []									## Essentially, the created_time field gives me the date and time of each post, but not the day of the week
															## Therefore, datetime module must be imported
		for my_post in my_list_of_posts:			## For each post in my list of 100 posts, I want its day, month and year posted

			post_year = my_post['created_time'][:4]		## Slicing created_time field (string) in my_list_of_posts for only the year of each post
			post_month = my_post['created_time'][5:7]	## Now, slicing created_time field (string) for only the motnh of each post
			post_day = my_post['created_time'][8:10]	## Slicing for only the day of each post

			my_tuple = (post_year, post_month, post_day)				## Creating tuple of date of post so datetime module can convert/find appropriate weekday
			day_of_the_week = datetime.datetime(int(post_year), int(post_month), int(post_day))		## Converting tuple strings (of created_time) into integers so datetime module can function properly
			my_assignment = day_of_the_week.weekday()								## Proper documentation for the correct assignments of weekdays to their specific integers

			if my_assignment == 6:		## If the returned integer is 6, then that post's day of the week is Sunday
				day_of_the_week = 'Sunday'

			elif my_assignment == 0:		## If the returned integer is 0, then that post's day of the week is Monday
				day_of_the_week = 'Monday'

			elif my_assignment == 1:		## Process continues for the remaining weekdays...
				day_of_the_week = 'Tuesday'

			elif my_assignment == 2:
				day_of_the_week = 'Wednesday'

			elif my_assignment == 3:
				day_of_the_week = 'Thursday'

			elif my_assignment == 4:
				day_of_the_week = 'Friday'

			elif my_assignment == 5:
				day_of_the_week = 'Saturday'

			list_of_weekdays.append(day_of_the_week)			## Appending the day of the week of each post to the larger list (list_of_weekdays)


		complete_dictionary = {}					## Making a complete dictionary to store the three data points (weekday, number of likers, number of comments) with their corresponding post ID
		for x in range(len(list_of_post_ids)):			## Ensuring that I am iterating over every single post_id
			complete_dictionary[list_of_post_ids[x]] = (list_of_weekdays[x], list_of_number_of_likers[x], list_of_number_of_comments[x])		## Structuring the key/values of my complete dictionary

	
		CACHE_DICTION[my_user_id] = complete_dictionary			## Adding my new dictionary (with new fetched data) to cached dictionary
		my_cached_data = complete_dictionary						 

		pprint(complete_dictionary)		## Output

		writing_file = open(CACHE_FNAME, 'w')				## Opening cache file in order to write in it
		writing_file.write(json.dumps(CACHE_DICTION))			## Writing this new cached dictionary to my cache file
		writing_file.close()							## Finished writing, closing cache file

		## Report Part 1:
		## Finding Activity for Each Weekday 								## Essentially finding frequency

		dictionary_of_weekday_frequencies = {}							## Initializing empty frequency dictionary
		for my_key in complete_dictionary:									## Iterating over my large dictionary (that has my three data points)
			weekday_string = str(complete_dictionary[my_key][0])				## Accessing only the weekday via indexing			
			if weekday_string in dictionary_of_weekday_frequencies:			## After iterating through large complete_dictionary, if we have already seen specific weekday, add to it's frequency value by 1
				dictionary_of_weekday_frequencies[weekday_string] += 1
			else:
				dictionary_of_weekday_frequencies[weekday_string] = 1 			## Don't increment/add to weekday's frequency value otherwise

		sorted_dictionary = sorted(dictionary_of_weekday_frequencies.items(), key=lambda x: x[1], reverse = True) 	## Sorting my weekday frequency dictionary by its values in descending order (from greatest to least). Converted into a list of tuples.  

		print('\n')
		print('Social Media Report - File Output of Post Frequency (For Each Weekday)')
		print('\n')
		print(sorted_dictionary)	
		print('\n')	

	return my_cached_data


## SQL Setup

my_database = sqlite3.connect('Facebook_Posts.db')			## Creating connection to new database 
cur = my_database.cursor()								## Variable that holds cursor

cur.execute('DROP TABLE IF EXISTS Facebook_Posts')
cur.execute('CREATE TABLE Facebook_Posts (post_id TEXT, weekday_posted TEXT, number_of_likers NUMBER, number_of_comments NUMBER)')			## Establishing the specific columns (post_id, weekday_posted, number_of_likers, and number_of_comments) for my Facebook_Posts database, where I will place the corresponding data for each of the 100 posts 

facebook_posts = getFacebookData(Facebook_Info.my_access_token)		## Invoking the large function that will return a dictionary of 100 posts on the specified user's feed/timeline/wall. The value of each post (key) is a list containing the weekday it was posted, the number of likers and number of comments

for my_var in facebook_posts.keys():
	my_tup = str(my_var), str(facebook_posts[my_var][0]), int(facebook_posts[my_var][1]), int(facebook_posts[my_var][2])						## Grabbing the Facebook data I want to insert into my database, while converting into appropriate data type - so that it corresponds to correct database format (e.g., NUMBER, TEXT)
	cur.execute('INSERT INTO Facebook_Posts (post_id, weekday_posted, number_of_likers, number_of_comments) VALUES (?, ?, ?, ?)', my_tup)			## Executing my insert statements (inserting Facebook data into their appropriate database columns)

my_database.commit()		## Supposed to commit changes after altering database tables

cur.close()
my_database.close()			## Closing database connection

