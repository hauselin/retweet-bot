#%%

import tweepy

#%%


def tweepy_auth(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET):
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api


def retweet_favorites(api, username, count=5):
    tweet_list = api.favorites(screen_name=username, count=count)
    for tweet in tweet_list:
        print(tweet.id)
        try:
            api.retweet(tweet.id)
            print("retweeted")
        except tweepy.TweepError as e:
            print(e)
    return print("done.")