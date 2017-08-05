# sentiments
The result of each input is p/t where p is the number of tweets found to be positive over the total number of tweets found.

Using terminal execute the tweet_Sentiment.py script followed by 'keyword(s)' in quotes that are of interest to you (no need to seperate them with a comma).
```
python3 tweet_Sentiment.py 'filecoin' 'Blue' 'Trump' 'Obama'
```



The script will use Twitter's API to query for the keyword and return a maximum of 100 tweets containing your keyword. 
Each tweet will be evaluated independently and count as a +1 positive tweet or 0 if not. 
Every word in a tweet is searched for in the file "SentiWordNet_3.0.0_20130122.txt" if found its positive and negative score will be added to the tweets overall score. 

For each tweet the sum of all positive word scores and negative word scores determines whether the tweet is +1 or 0. 
     - Positive ＞ Negative = +1
     - Positive ≤ Negative = 0



**EXAMPLE INPUT:**
```
python3 tweet_Sentiment.py 'filecoin' 'Blue' 'Trump' 'Obama'
```

**OUTPUT:**
```
filecoin  Positive sentiments\total tweets: 81\100
Blue  Positive sentiments\total tweets: 33\100
Trump  Positive sentiments\total tweets: 57\100
Obama  Positive sentiments\total tweets: 71\100
```

In addition the Twitter API request use and remainders will be printed before and after the script places its requests. If any of the Twitter API requests reache 0 twitter will temporarily block you.
```
Used:2  Remaining:178  application/rate_limit_status
Used:4  Remaining:176  search/tweets
```




- [x] Evaluate sentiment of tweets
- [x] Print Twitter API counter
- [ ] Add SMS language conversion of tweets
- [ ] Correct lolzzz speeeeech (remove extra characterssss & ?)
- [ ] Consider preventing retweets from evaluation

The evaluation of each tweet is based upon the sentiment assement of each word which was provided by SentiWordNet:

> The file "SentiWordNet_3.0.0_20130122.txt" is built upon SentiWordNet 3.0.0 (2013). It is "made freely available for research purposes" by Andrea Esuli and Fabrizio Sebastiani at Istituto di Scienza e Tecnologie dell’Informazione, Consiglio Nazionale delle Ricerche http://sentiwordnet.isti.cnr.it/

> The file used here is a condensed version of the SentiWordNet version and should be updated (or prempted by) SMS language conversion https://en.wikipedia.org/wiki/SMS_language



