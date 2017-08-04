#!/usr/bin/env python3 -B

# tweet_SearchAnalysis.py
# Import necessary libraries
import codecs
import json
import tweepy
from string import punctuation
# Uses SentiWordNet_3.0.0_20130122.txt from
# http://sentiwordnet.isti.cnr.it/
# https://stackoverflow.com/questions/38263039/sentiwordnet-scoring-with-python

def get_twitter_api():
    #### Load API keys file
    keys_json = json.load(open('/usr/local/keys.json'))
    #### Specify key dictionary wanted (generally [Platform][User][API])
    #Keys = keys_json["Twitter"]["ClimateCong_Bot"]["ClimatePolitics"]
    Keys = keys_json["Twitter"]["AGreenDCBike"]["HearHerVoice"]
    #### Access API using key dictionary definitions
    auth = tweepy.OAuthHandler( Keys['Consumer Key (API Key)'], Keys['Consumer Secret (API Secret)'] )
    auth.set_access_token( Keys['Access Token'], Keys['Access Token Secret'] )
    api = tweepy.API(auth)
    return(api)




#### Define Twitter API rates determining loop
#Follow add rate limited to 1000 per 24hrs: https://support.twitter.com/articles/15364
def twitter_API_rates():
    api = get_twitter_api()
    rate_limits = api.rate_limit_status()['resources']
    new = str(rate_limits).split("'/")
    for anew in new[1:]: #skip the first one item it is not a limit key
        limit_value = (anew.split("':"))[0]
        anew_json = (anew[anew.find("{"):anew.find("}")+1]).replace("'",'"')
        vals = json.loads(anew_json)
        c = vals['limit']
        #d = vals['reset']
        e = vals['remaining']
        f = c-e
        if f != 0:
            #print(anew)
            print("Used:" + str(f) + "  Remaining:" + str(e) + "  " + limit_value)
        else:
            pass




class tweet_SearchAnalysis():
    api = get_twitter_api()

    # Load the list of positive and negative words
    # These will be used for analysing the tweets
    SentiWordNet = open("SentiWordNet_3.0.0_20130122.txt").read()
    SentiWordNet = SentiWordNet.split('\n')
    SentiPOS = []
    SentiID = []
    SentiPosS = []
    SentiNegS = []
    SentiWords = []
    for line in SentiWordNet:
        split_line = line.split(',')
        SentiPOS.append(split_line[0])
        SentiID.append(split_line[1])
        SentiPosS.append(split_line[2])
        SentiNegS.append(split_line[3])
        SentiWords.append(split_line[4])

        # tweetSearch() searches for 100 tweets containing the "keyword name"
        # and saves them to "Tweets_on_X.txt" for sentiment analysis at
        # tweetSentimentAnalysis
        def tweetSearch(self, keywordName):
            #print(keywordName)
            outFile = codecs.open("Tweets_on_" + keywordName + ".txt", 'w', "utf-8")
            results = self.api.search(q=keywordName, lang="en", locale="en", count=100)
            for result in results:
                #print(result.id_str)
                outFile.write("https://twitter.com/anon/status/" + result.id_str + " " + (result.text).replace("\n","  ") + '\n')
            outFile.close()


        # This is the core of the analysis logic
        # I've kept it really simple, i.e., count the total number
        # of positive and negative words cumulated across all the
        # tweets stored in "testTweets.txt" and decide the sentiment.
        def posCount(self, tweet):
            pos = 0
            neg = 0
            for p in list(punctuation):
                tweet = tweet.replace(p, '')
            tweet = tweet.lower() #.encode('utf8')
            words = tweet.split(' ')

            for word in words:
                if word in self.SentiWords:
                    # i is a list of positions of 'word' within the SentiWords list
                    i=[ind for ind,p in enumerate(self.SentiWords) if p==word]
                    i[0] # Only use the first occurence (later specify A/V/N)
                    pos = pos + float(self.SentiPosS[i[0]])
                    neg = neg + float(self.SentiNegS[i[0]])
            if neg < pos:
                a_tweet_sentiment = 1
                #print("Tweet is positive: 1")
                #print(neg,pos)
            else:
                a_tweet_sentiment = 0
                #print("Tweet is negative or null: 0")
                #print(neg,pos)
            return a_tweet_sentiment

        def tweetSentimentAnalysis(self, keywordName):
            #print(keywordName)
            # Read all the tweets from "Tweets_on_ X.txt" and
            # split + store them to tweets_list
            tweets = codecs.open("Tweets_on_" + keywordName + ".txt", 'r', "utf-8").read()
            tweets_list = tweets.split('\n')
            #tweets.close()           - AttributeError: 'str' object has no attribute 'close'
            tweets_sent = 0
            tweet_number = 0
            for tweet in tweets_list:
                if(len(tweet)):
                    a_tweet_sent = self.posCount(tweet)
                    tweets_sent += a_tweet_sent
                    tweet_number += 1

            #Printing Results
            pos_sentiment_and_total = str(tweets_sent) + "\\" + str(tweet_number)
            print(keywordName + "  Positive sentiments\\total tweets: " + pos_sentiment_and_total)
            return (pos_sentiment_and_total)
