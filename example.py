#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

CONSUMER_KEY = 'x'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'x'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = 'x'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'x'#keep the quotes, replace this with your access token secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# target = open("x", 'w')

# for x in range (0, 10):
#         for tweet in api.user_timeline(user_id = "x", count = "10000", page = x):
#                 target.write(tweet.text + "\n")

#http://docs.tweepy.org/en/latest/api.html#API.search
# for x in tweepy.Cursor(api.search, q='SAS Analytics').items(100):
# 	print x.text + "\n"

                

