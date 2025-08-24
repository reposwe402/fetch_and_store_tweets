import tweepy
from config import consumer_key, consumer_secret, access_token, access_token_secret

class TwitterClient:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)

    def search_tweets(self, hashtag, since_date="2017-04-03", count=100, lang="en"):
        return tweepy.Cursor(self.api.search, q=hashtag, count=count, lang=lang, since=since_date).items()
