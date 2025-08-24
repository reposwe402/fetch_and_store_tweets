from twitter_client import TwitterClient
from data_storage import DataStorage
from config import tag


def main():
    # Initialize Twitter client and data storage
    twitter_client = TwitterClient()
    data_storage = DataStorage()

    try:
        # Fetch and store tweets
        for tweet in twitter_client.search_tweets(hashtag=tag):
            data_storage.store_tweet(tweet.created_at, tweet.text)
    finally:
        # Ensure the file is closed properly
        data_storage.close()


if __name__ == "__main__":
    main()
