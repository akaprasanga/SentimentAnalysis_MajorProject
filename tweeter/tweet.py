import tweepy
import csv
import pandas as pd
import configparser
import re
import emoji

config = configparser.RawConfigParser()
config.read('tokens.cfg')
consumer_key = config.get('Main','consumer_key')
consumer_secret = config.get('Main','consumer_secret')
access_token = config.get('Main','access_token')
access_token_secret = config.get('Main','access_token_secret')


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
print(api)
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

# for tweet in tweepy.Cursor(api.search,q="#bitcoin",count=100,
#                            lang="en",
#                            since="2017-02-2").items(10):
#     print (tweet.created_at, tweet.text)
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])




# filtering the urls mentions and emojis from the tweets
def giveFilteredTweet(text):
    emoji_pattern = re.compile(
    u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    "+", flags=re.UNICODE)
    emojiFiltered = emoji_pattern.sub(r'', text)
    refine_urls = re.sub(r'(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+','',emojiFiltered)
    refine_mentions = re.sub(r'@[A-Za-z0-9]+','',refine_urls)
   
    return refine_mentions




for tweets in tweepy.Cursor(api.user_timeline,id="BitcoinForums", count=100, lang="en").items(0):
    review = giveFilteredTweet(tweets.text)
    print(tweets.created_at, review)

    csvWriter.writerow([tweets.created_at, review])