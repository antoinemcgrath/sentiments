# tweet_Sentiment.py
# python3 tweet_Sentiment.py 'filecoin' 'Blue' 'Trump' 'Obama'

# Import necessary libraries
import codecs
import tweet_SearchAnalysis # Custom library to pull, store, analyse relevant tweets and returns the sentiment
import sys
search_words = sys.argv[1:]
this_list = ["Test"] #Test Standard
#this_list = ["Climate Change", "Global Warming", " SB32 "] #Standard
#this_list = ["Donald J Trump", "Texas", "Kansas", "Peach", "Plum", "Car", "Frown", "CNN", "FOX", "News", "Monday", "Mon", "Tuesday", "Tues", "Wednesday", "Wedn", "Thursday", "Thur", "Friday", "Fri", "Saturday", "Sat", "Sunday", "Sun", "Nude", "Scarf", "Archive", "AAPL", "BRK.A", "GOOG", "HPQ", "INTC", "MMM", "MSFT", "TGT", "WMT"]
# Stock tickers    #A – Agilent Technologies    #AAPL – Apple Inc.    #BRK.A – Berkshire Hathaway (class A shares)    #C – Citigroup    #GOOG – Alphabet Inc.    #HOG – Harley-Davidson Inc.    #HPQ – Hewlett-Packard    #INTC – Intel    #KO – The Coca-Cola Company    #LUV - Southwest Airlines (after their main hub at Love Field)    #MMM – Minnesota Mining and Manufacturing (3M)    #MSFT – Microsoft    #T - AT&T    #TGT – Target Corporation    #TXN – Texas Instruments #WMT – Walmart
this_list = search_words

tweet_SearchAnalysis.twitter_API_rates()


def keyword_var_pac():
    nameOfkeywords = []
    keywordNameList = []
    keywordKeyValue = {}
    counter = 0
    print(this_list)
    for one_name in this_list:
        keywordKeyValue[counter] = {}
        keywordNameList.append(one_name)
        keywordName = one_name
        keywordKeyValue[counter]["keywordName"] = keywordName
        counter += 1
        #print(type(nameOfkeywords))
        #print((nameOfkeywords))
        #print(type(keywordKeyValue))
        #print((keywordKeyValue))
    return nameOfkeywords, keywordKeyValue


if __name__ == '__main__':
    nameOfkeywords, keywordKeyValue = keyword_var_pac()
    keyword = tweet_SearchAnalysis.tweet_SearchAnalysis()
    # Final output will be stored at "Keyword_Sentiment_Results.txt"
    outputFile = codecs.open("Keyword_Sentiment_Results.txt", 'w', "utf-8")

    # Sentiment on of keywords
    repeat_num = len(keywordKeyValue)
    #print(keywordKeyValue)
    for i in range(repeat_num):

        keywordName = keywordKeyValue[i]["keywordName"]
        keyword.tweetSearch(keywordName)
        # Sentiment is calculated on keywords
        keywordKeyValue[i]["tweet_Sentiment"] = keyword.tweetSentimentAnalysis(keywordName)
        #print("Word searched for: " + keywordKeyValue[i]["keywordName"])
        #print("Overall Sentiment on Twitter: " + keywordKeyValue[i]["tweet_Sentiment"] + "\n")
        #print(keywordKeyValue[i])
        outputFile.write("Word searched for: " + keywordKeyValue[i]["keywordName"] + "\n")
        outputFile.write("Overall Sentiment on Twitter: " + str(keywordKeyValue[i]["tweet_Sentiment"]) + "\n")
        outputFile.write("\n")
    outputFile.close()
tweet_SearchAnalysis.twitter_API_rates()
