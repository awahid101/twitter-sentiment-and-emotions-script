from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

class Sentiment(object):

    def get_polarity(self, text):
        blob = TextBlob(text)
        return blob.sentiment.polarity
    
    def get_sentiment(self, text):
        blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
        return blob.sentiment