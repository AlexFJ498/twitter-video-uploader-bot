import os
import tweepy

# Obtain keys
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
bearer_token = os.getenv('BEARER_TOKEN')

# Authenticate to Twitter using API V1.1
auth1 = tweepy.OAuth1UserHandler(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)
api = tweepy.API(auth1)

# Authenticate to Twitter using API V2
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Upload video
video = open('video.mp4', 'rb')
response = api.media_upload(filename='video.mp4', file=video)
media_id = response.media_id

# Create tweet
response = client.create_tweet(text='', media_ids=[media_id])
