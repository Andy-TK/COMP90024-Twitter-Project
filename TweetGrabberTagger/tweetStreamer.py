# tweetStreamer.py
# ~Jun Min (542339)

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
from argParser import ArgParser
from config import Config
from geoTool import BoundingBox
from tweetTagger import tweetTagger

# Bounding Box
bounding_box = BoundingBox(Config.longitude,
        Config.latitude, Config.search_radius)

class TweetAnalysisListener(StreamListener):
    """ Listener handler that passes tweets for analysis"""

    def __init__(self, f, ip, port):
        '''Initializes write to file and api args'''
        self.f = f
        self.ip = ip
        self.port = port

        self.count = 0

    def on_data(self, data):

        tagged_tweet = tweetTagger(json.loads(data)) # Load raw JSON into dict
        json_tagged_tweet = tagged_tweet.getJSONTaggedTweet()

        # Decide what to do with the tweet
        self.f.write(data) # Temporarily

        self.count += 1
        print(self.count)

        return True

    def on_error(self, status):
        # Crap, rate limit reached
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
        print(status)

# Main Entry
if __name__ == '__main__':

    # Arg Parsing
    ap = ArgParser()
    args = ap.getArgs()

    if (args.dump):
        f = open(args.dump,'a+')
        #f.close()
    else:
        f = None

    print("Boundary:",bounding_box)

    tal = TweetAnalysisListener(f, args.ip, args.port)
    auth = OAuthHandler(Config.consumer_key, Config.consumer_secret)
    auth.set_access_token(Config.access_token, Config.access_token_secret)

    stream = Stream(auth, tal)
    stream.filter(locations=bounding_box)

