from tweepy import API 
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import os
import webbrowser

from textblob import TextBlob

import matplotlib.pyplot as plt 
import twitter_credentials

import numpy as np
import pandas as pd
import re
import csv

def percentage(part, whole):
    return 100 * float(part) / float(whole)

# TWITTER CLIENT
class TwitterClient():
    def __init__(self, twitter_user=None):
        # Here twitter_user parameter is defualt to none, and need to specify user.
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)

        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

# TWITTER AUTHENTICATER
class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth

# TWITTER STREAMER
class TwitterStreamer():
    
    # Class for streaming and processing live tweets.
    
    def __init__(self):
        self.twitter_autenticator = TwitterAuthenticator()    

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming api.
        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_autenticator.authenticate_twitter_app() 
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords.
        stream.filter(track=hash_tag_list)

# TWITTER STREAM LISTENER
class TwitterListener(StreamListener):

    # This is a basic listener that just prints received tweets to terminal.

    def __init__(self, fetched_tweets_filename):
        #Constructor
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
            # Appened it here, because we continuely want to add the tweets as we stream.
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          
    def on_error(self, status):
        if status == 420:
            # Returning False on_data method in case limit exceeds.
            return False
        print(status)

class TweetAnalyzer():

    # Functionality for analyzing and categorizing content from tweets.
    
    def clean_tweet(self, tweet): 
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyze_sentiment(self, tweet):

        analysis = TextBlob(self.clean_tweet(tweet))

        if (analysis.sentiment.polarity == 0):
            return "Neutral"                          
        
        elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.3):
            return "Weakly_Positive"        #0.1,0.2,0.3                  
        
        elif (analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.6):
            return "Positive"               #0.4,0.5,0.6                  
        
        elif (analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <= 1):
            return "Strongly_Positive"      #0.7,0.8,0.9,1                
        
        elif (analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= 0):
            return "Weakly_Negative"        #0,-0.2,-0.1                  
        
        elif (analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <= -0.3):
            return "Negative"               #0,-0.5,-0.4,-0.3
        
        elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.6):
            return "Strongly_Negative"      #0,-0.9,-0.8,-0.7,-0.6 

    def tweets_to_data_frame(self, tweets):
        pd.options.display.max_colwidth = 100
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
        
        """ DataFrame(), function from pandas that allows to create a data frame 
            on the content that have been added to it. """

        return df
 
if __name__ == '__main__':

    ####    FOR 1ST NEWS CHANNEL    ####

    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()

    api = twitter_client.get_twitter_client_api()

    tweets = api.user_timeline(screen_name="geonews_english", count=50)

    df = tweet_analyzer.tweets_to_data_frame(tweets)
    df['Sentiment'] = np.array([tweet_analyzer.analyze_sentiment(tweet) for tweet in df['Tweets']])

    with open('GEO_Sentiments.csv', 'w', encoding='utf-8') as f:
        csvfile = csv.writer(f, delimiter='\n')
        csvfile.writerow(df['Sentiment'])
   
    
    with open('C:/WampServer/www/SentimentAnalysis/1stNews.txt', 'w', encoding="utf-8") as f:
        print(df['Tweets'], file=f)

    positive = 0
    negative = 0
    wpositive = 0
    wnegative = 0
    spositive = 0
    snegative = 0
    neutral = 0 

    with open('GEO_Sentiments.csv', 'r') as f:
        for line in f:
            words = line.split()
            for i in words:
                if (i == "Neutral"):
                    neutral += 1
                elif (i == "Weakly_Positive"):
                    wpositive += 1
                elif (i == "Positive"):
                    positive += 1
                elif (i == "Strongly_Positive"):
                    spositive += 1
                elif (i == "Weakly_Negative"):
                    wnegative += 1
                elif (i == "Negative"):
                    negative += 1
                elif (i == "Strongly_Negative"):
                    snegative += 1

    
    wpositive = percentage(wpositive,50)
    positive = percentage(positive,50)
    spositive = percentage(spositive,50)
    neutral = percentage(neutral,50)
    snegative = percentage(snegative,50)
    negative = percentage(negative,50)
    wnegative = percentage(wnegative,50)


    names = ["Weakly Positive", "Positive", " Strongly Positive", "Neutral", "Weakly Negative", "Negative", "Strongly Negative"] 
    positions = [0,1,2,3,4,5,6]
    scores = [wpositive,positive,spositive,neutral,wnegative,negative,snegative]

    plt.bar(positions, scores, width= 0.2)


    ####    FOR 2ND NEWS CHANNEL    ####

    twitter_client2 = TwitterClient()
    tweet_analyzer2 = TweetAnalyzer()

    api2 = twitter_client2.get_twitter_client_api()

    tweets = api2.user_timeline(screen_name="aaj_news", count=50)

    df2 = tweet_analyzer2.tweets_to_data_frame(tweets)
    df2['Sentiment'] = np.array([tweet_analyzer2.analyze_sentiment(tweet) for tweet in df2['Tweets']])

    with open('AAJ_Sentiments.csv', 'w', encoding='utf-8') as f:
        csvfile = csv.writer(f, delimiter='\n')
        csvfile.writerow(df2['Sentiment'])

    with open('C:/WampServer/www/SentimentAnalysis/2ndNews.txt', 'w', encoding="utf-8") as f:
        print(df2['Tweets'], file=f)
    
    positive = 0
    negative = 0
    wpositive = 0
    wnegative = 0
    spositive = 0
    snegative = 0
    neutral = 0 

    with open('AAJ_Sentiments.csv', 'r') as f:
        for line in f:
            words = line.split()
            for i in words:
                if (i == "Neutral"):
                    neutral += 1
                elif (i == "Weakly_Positive"):
                    wpositive += 1
                elif (i == "Positive"):
                    positive += 1
                elif (i == "Strongly_Positive"):
                    spositive += 1
                elif (i == "Weakly_Negative"):
                    wnegative += 1
                elif (i == "Negative"):
                    negative += 1
                elif (i == "Strongly_Negative"):
                    snegative += 1

    wpositive = percentage(wpositive,50)
    positive = percentage(positive,50)
    spositive = percentage(spositive,50)
    neutral = percentage(neutral,50)
    snegative = percentage(snegative,50)
    negative = percentage(negative,50)
    wnegative = percentage(wnegative,50)

    positions2 = [0.2,1.2,2.2,3.2,4.2,5.2,6.2]
    scores2 = [wpositive,positive,spositive,neutral,wnegative,negative,snegative]

    plt.bar(positions2, scores2, width= 0.2, color= 'g')

    ####    FOR 3RD NEWS CHANNEL    ####

    twitter_client3 = TwitterClient()
    tweet_analyzer3 = TweetAnalyzer()

    api3 = twitter_client3.get_twitter_client_api()

    tweets = api3.user_timeline(screen_name="arynewsofficial", count=50)

    df3 = tweet_analyzer3.tweets_to_data_frame(tweets)
    df3['Sentiment'] = np.array([tweet_analyzer3.analyze_sentiment(tweet) for tweet in df3['Tweets']])

    with open('ARY_Sentiments.csv', 'w', encoding='utf-8') as f:
        csvfile = csv.writer(f, delimiter='\n')
        csvfile.writerow(df3['Sentiment'])

    with open('C:/WampServer/www/SentimentAnalysis/3rdNews.txt', 'w', encoding="utf-8") as f:
        print(df3['Tweets'], file=f)

    positive = 0
    negative = 0
    wpositive = 0
    wnegative = 0
    spositive = 0
    snegative = 0
    neutral = 0 

    with open('ARY_Sentiments.csv', 'r') as f:
        for line in f:
            words = line.split()
            for i in words:
                if (i == "Neutral"):
                    neutral += 1
                elif (i == "Weakly_Positive"):
                    wpositive += 1
                elif (i == "Positive"):
                    positive += 1
                elif (i == "Strongly_Positive"):
                    spositive += 1
                elif (i == "Weakly_Negative"):
                    wnegative += 1
                elif (i == "Negative"):
                    negative += 1
                elif (i == "Strongly_Negative"):
                    snegative += 1

    wpositive = percentage(wpositive,50)
    positive = percentage(positive,50)
    spositive = percentage(spositive,50)
    neutral = percentage(neutral,50)
    snegative = percentage(snegative,50)
    negative = percentage(negative,50)
    wnegative = percentage(wnegative,50)

    positions3 = [0.4,1.4,2.4,3.4,4.4,5.4,6.4]
    scores3 = [wpositive,positive,spositive,neutral,wnegative,negative,snegative]

    
    plt.bar(positions3, scores3, width= 0.2, color= 'y')
    #plt.title("Sentiment Analysis between 3 News Channels")
    plt.legend(["1st News", "2nd News", "3rd News"])
    plt.ylabel("Percentage\n")
    plt.xlabel("\nSentimental Polarity Levels")
    plt.yticks([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100], 
    ['0%','5%','10%','15%','20%','25%','30%','35%','40%','45%','50%','55%','60%',
    '65%','70%','75%','80%','85%','90%','95%','100%'])
    plt.xticks(positions2, names)
    plt.tight_layout()
    #plt.savefig('C:/WampServer/www/SentimentAnalysis/Images/FinalComparison.svg', dpi=500)
    fig = plt.gcf()
    fig.set_size_inches((10, 6), forward=False)
    fig.savefig('C:/WampServer/www/SentimentAnalysis/Images/FinalComparison.svg', dpi=500)

    os.system('python Plotting.py')
    webbrowser.open('http://localhost/SentimentAnalysis/webpage.php')  