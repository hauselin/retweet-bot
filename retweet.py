#%%

import tweepy
import os
from dotenv import load_dotenv

#%% authenticate

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

#%%

tweet_list = api.favorites(screen_name="stephenfry", count=5)
# len(tweet_list)

#%% retweet each tweet favorited by user/screen_name above

for tweet in tweet_list:
    print(tweet.id)
    try:
        api.retweet(tweet.id)
        print("retweeted")
    except tweepy.TweepError as e:
        print(e)

#%%

# id = api.get_user("hauselin").id
# api.send_direct_message(id, "hey can you respond please")

# api.home_timeline(count=2)

for tweet in tweet_list:
    print(tweet.created_at)
    print(tweet.text)
    print("\n")

#%%

t = api.get_status(1050118621198921728)
t.text
idx = t.entities["urls"][0]["indices"]
t.text[idx[0] : idx[1]]

#%%

api.get_status()
api.home_timeline(count=1)

ts = api.user_timeline(count=2)
ts[0].entities

res = api.search("https://www.nytimes.com/live/2021/01/27/us/biden-trump-impeachment")
len(res)


#%% 


for t in res:
    print(t.)
    print(t.text, end="\n\n")
    

#%% 
