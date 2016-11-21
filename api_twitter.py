
import tweepy, time, sys
from lxml import html
import requests
from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np 


#Define api keys
CONSUMER_KEY  = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET  =''

#Connection to the twitter API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#Generate 50 click on a tweet, we need to specify the tweet url
#for i in range(50):
	#git = requests.get(url_tweet)

#Command to update the statue of twitter accounter
#api.update_status()

Name_User = ""
timeline  = api.user_timeline(screen_name=Name_user)

# We can retweet each tweet on timeline
# for tweet in timeline:
# try:  api.retweet(tweet.id)
# except  : print(tweet.id)


#We get some information about name_user
user = api.get_user(screen_name = Name_user)
print ("User id: " + user.id_str)
print (user.name)
print ("Description: " + user.description)
print ("Language: " + user.lang)
print ("Account created at: " + str(user.created_at))
print ("Location: " + user.location)

print ("Number of tweets: " + str(user.statuses_count))
print ("Number of followers: " + str(user.followers_count))
print ("Following: " + str(user.friends_count))
print ("A member of " + str(user.listed_count) + " lists.")

#All information tweet
for tweet in timeline:                                              
    ...:         print ("ID:", tweet.id)
    ...:         print ("User ID:", tweet.user.id)
    ...:         print ("Text:", tweet.text)
    ...:         print ("Created:", tweet.created_at)
    ...:         print ("Geo:", tweet.geo)
    ...:         print ("Contributors:", tweet.contributors)
    ...:         print ("Coordinates:", tweet.coordinates) 
    ...:         print ("Favorited:", tweet.favorited)
    ...:         print ("In reply to screen name:", tweet.in_reply_to_screen_nam
    ...: e)
    ...:         print ("In reply to status ID:", tweet.in_reply_to_status_id)
    ...:         print ("In reply to status ID str:", tweet.in_reply_to_status_i
    ...: d_str)
    ...:         print ("In reply to user ID:", tweet.in_reply_to_user_id)
    ...:         print ("In reply to user ID str:", tweet.in_reply_to_user_id_st
    ...: r)
    ...:         print ("Place:", tweet.place)
    ...:         print ("Retweeted:", tweet.retweeted)
    ...:         print ("Retweet count:", tweet.retweet_count)
    ...:         print ("Source:", tweet.source)
    ...:         print ("Truncated:", tweet.truncated)





