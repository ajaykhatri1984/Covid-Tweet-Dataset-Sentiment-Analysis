import twint
import pandas as pd
import json
from pandas.io.json import json_normalize


import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 



import pandas as pd
import csv

filename = 'tweetsDBeconomy1Lakh.csv'

def getTweets():
    c = twint.Config()
    c.Search = "Covid 19 economy"#"Covid 19 impact on education"
    c.Lang = "En"
    c.Limit = 100000
    c.Output = filename
    twint.run.Search(c)


def get_tweet_sentiment(tweet): 
    analysis = TextBlob(clean_tweet(tweet)) 
    print(analysis)
    # set sentiment 
    if analysis.sentiment.polarity > 0: 
        return 'Positive'
    elif analysis.sentiment.polarity == 0: 
        return 'Neutral'
    else: 
        return 'negative'
def clean_tweet(tweet):         
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 



def createSentimentDatasetFromRawTweet():
    data = []
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for tweet in reader:
            tweet = str(tweet)
            user = tweet[2:21]
            d1 = tweet[22:47]#fetch date      
            tweet = tweet[48:]#fetch tweet
            #tweet  = clean_tweet(tweet) 
            result = get_tweet_sentiment(tweet)      
            #print((d1,tweet,result))
            data.append((user,'','',d1,tweet,result))
        
        df = pd.DataFrame(data, columns =['UserName','ScreenName',	'Location',	'TweetAt',	'OriginalTweet'	,'Sentiment'])

        df.to_csv('dataset-'+ filename,index=False)

getTweets()

createSentimentDatasetFromRawTweet();

