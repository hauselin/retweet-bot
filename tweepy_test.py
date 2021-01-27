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

user = api.get_user("hauselin")
print(user.screen_name)
print(user.followers_count)

#%%

# api.update_status(status="Hello!")
# api.update_status(status="Hi there!")

#%%

print("FINISH!\n")
