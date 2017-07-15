#import requests.packages.urllib3
#requests.packages.urllib3.disable_warnings()
import tweepy
import time,json
import numpy as np
import tweepy as TweepError
def find_first(vec,item):
    """return the index of the first occurence of item in vec"""
    for i in range(500):
	for j in range(2):
           if item == vec[i][j]:
             return i
    return -1
#finding max
def find_max(vec):
    """return the largest item in vec"""
    high=vec[0][1]
    highid=vec[0][0]
    for i in range(100):
	for j in range(2):
           if (high<vec[i][1]):
             high=vec[i][1]
	     highid=vec[i][0]
    return highid

APP_KEY="write own"
APP_SECRET="write own"
OAUTH_TOKEN="write own"
OAUTH_TOKEN_SECRET="write own"
username=raw_input(" find biggest fan of : ")
auth = tweepy.OAuthHandler(APP_KEY,APP_SECRET)
auth.set_access_token(OAUTH_TOKEN,OAUTH_TOKEN_SECRET)

count=0
i=0
j=0
api = tweepy.API(auth)

row_num = 50000
col_num = 2
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
new_tweets = api.user_timeline(screen_name = username,count=200,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
	
#save most recent tweets
alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
oldest = alltweets[-1].id - 1
while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = username,count=200,max_id=oldest,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
print "...%s tweets downloaded so far" % (len(alltweets))

for tweet in alltweets:
    
       #firstTweet = api.user_timeline(screen_name=username,include_rts=0,count=200)[j]
       if hasattr (tweet, 'retweeted_status'):
    	# get the original tweet
    	original_tweet = tweet.retweeted_status.id
    	# iterate over retweets to get user id
	#a=np.array(multi_list)
    	for status1 in api.retweets(original_tweet,wait_on_rate_limit=True,wait_on_rate_limit_notify=True):
	  # b=np.where(a==status1.user.id)
	   b=find_first(multi_list,status1.user.id)
#	   print (b)
	   if(b!=-1):
	      multi_list[b][1]+=1
	   else:
     	      multi_list[i][0]=status1.user.id
      	      i+=1
       	   print status1.user.id
   
	   
#print("array\n")
#print(multi_list)
maxa=find_max(multi_list)
#print ("max=")
#print (maxa)
ty=api.get_user(user_id=maxa)
print "Biggest Fan of %s is %s"%(username,ty.screen_name)

			
