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
    consumer_key = 'YA7o8rljz2lr2lT6x0Pqm9GFJ'
    consumer_secret = 'Jju95zsOX05QPTQTFQi07sdF8zft4zgULYaZMe5rhrAAM3b3bo'
    access_token = '582758531-1kJSp9krnQ9UYNHRuwLkxdoF4JzzbR51Z0j8z4EV'
    access_secret = 'ihKcWlNAGXHEaSwEAL70OUdH1uleI7BDsNMf6PDRLT2td'
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