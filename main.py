from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from emotions import Emotion
from sentiments import Sentiment
import time
import json

#consumer key, consumer secret, access token, access secret.
ckey="FEIx7gT2VNBWqqWI5JbWr15rH"
csecret="ApUELHmBbmTVpTzI1rRf321WScENS3qzgv1DudZWJ6npACTlb32"
atoken="2931921560-zSy3fPD1DdsRJ7YcojmPoX28mHUr37Ux2xhJ8pAvx"
asecret="QKUiWBZALGE20kHOIa6dsSihWMoKN1lrNY2PC2yceHk3MNl"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        tweet = all_data["text"]
        username = all_data["user"]["screen_name"]
        
        #print tweet
        print tweet

        #get sentiment
        sentiment = Sentiment()

        #print sentiment
        print "Sentiment -"
        print sentiment.get_sentiment(tweet)
        print "-----"
        
        #get emotions
        emotion = Emotion()

        #print emotions
        print "Emotions -"
        print emotion.get_emotions(tweet)
        print "----"
        print ""

        return True

    def on_error(self, status):
        print status

#listen to the tweets on specific subject
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["obama"])
