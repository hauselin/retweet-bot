#%%

import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

#%% authenticate

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

#%%

tweet_list = api.favorites(screen_name="stephenfry", count=5)
len(tweet_list)
a = tweet_list[0]
type(a)
a.id
a.source
a.truncated
a.in_reply_t
a.user
a.text

# s = api.get_status(a.id)
# s.text
# api.retweet(a.id)

#%%

for tweet in tweet_list:
    print(tweet.id)
