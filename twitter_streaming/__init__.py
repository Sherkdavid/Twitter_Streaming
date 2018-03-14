import json
import tweepy
from tweepy import *
from textblob import TextBlob
import re
import os
import threading

class MyStreamListener(tweepy.StreamListener):

    def on_connect(self):
        print "Connection Established"

    def on_data(self, raw_data):
        stack.append(raw_data)

def clean_tweet(tweet):
    '''
    Borrowed regular expression
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def auth():
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_secret = ''
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(key=access_token,secret=access_secret)
    return auth

def main():
    api = tweepy.API(auth())
    listener = MyStreamListener(api=api)
    stream = tweepy.Stream(auth=api.auth, listener=listener)
    stream.filter(track=['Trump'],async=True)

stack = list()

if __name__ == "__main__":
    main()
