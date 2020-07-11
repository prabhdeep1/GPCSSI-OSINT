import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import wget 
import requests
import sys
import getopt
import os
import pandas as pd
import numpy as np


ACCESS_TOKEN = '2587900573-WV2E2gGjgLd990tQiciw8Ze34Z9mzSa3ARW6Ra8'
ACCESS_TOKEN_SECRET = 'NN0gJ0RF5KmWgj3De3T6mNWecV7FCbfdxJocp0p6SIS1U'
CONSUMER_KEY = 'y03mYHkiCCCmkAJxcFIIAQzv2'
CONSUMER_SECRET = 'Zfo3nqNAFkgsYp541sCSX12O6EqdcQTUuoAcgdSzGS9KQ1FToK'




auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

class TweetListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)
def info(username):
       api = tweepy.API(auth)
       twitterStream = Stream(auth,TweetListener())
       user = api.get_user(username)
       path="{}".format(username)
       os.mkdir(path)
       
       file1 = open('{}/{}.txt'.format(username,username),"w")
       file1.write(str(u"Name:{} \n".format(user.name).encode('utf-8')))

       file1.write(str(u"Location:{} \n".format(user.location).encode('utf-8')))
       file1.write(str(u"Description:{} \n".format(user.description).encode('utf-8')))
       file1.write(str(u"Created on: {} \n".format(user.created_at).encode('utf-8')))
       file1.write(str(u"Url Associated: {} \n".format(user.url).encode('utf-8')))
       file1.write(str(u"Profile Image: {} \n".format(user.profile_image_url).encode('utf-8')))
       file1.write(str(u"Total Followers: {} \n".format(user.followers_count).encode('utf-8')))
       file1.write(str(u"Status count: {} \n".format(user.statuses_count).encode('utf-8')))
       file1.write(str(u"Total following:{} \n".format(user.friends_count).encode('utf-8')))

       file1.close()
       print(u"Name:{} \n".format(user.name).encode('utf-8'))
       print(u"Location:{} ".format(user.location).encode('utf-8'))
       print(u"Description:{} ".format(user.description).encode('utf-8'))
       print(u"Created on: {} ".format(user.created_at).encode('utf-8'))
       print(u"Url Associated: {} ".format(user.url).encode('utf-8'))
       print(u"Profile Image: {} ".format(user.profile_image_url).encode('utf-8'))
       print(u"Total Followers: {} ".format(user.followers_count).encode('utf-8'))
       print(u"Status count: {} ".format(user.statuses_count).encode('utf-8'))
       print(u"Total following:{} ".format(user.friends_count).encode('utf-8'))

       
       
       target_path='{}/{}.jpg'.format(username,username)
       profile_pic=wget.download(user.profile_image_url,target_path)
       
       
       
       
       print("\nCreated {}.txt and profile pic of {}".format(username, username))   

            
        
def twiiter_media(username):
        api = tweepy.API(auth)
        tweets = api.user_timeline(screen_name=username,
                           count=200, include_rts=False,
                           exclude_replies=False)
        id=[]
        date=[]
        tweet_text=[]
        image_url=[]
        count = 1
        for status in tweets:  
                media = status.entities.get('media', [])
                user_mention = status.entities.get('user_mentions', [])
                if(len(media) > 0):
                       print("--------------------------------------------------###################################################------------------------------------")
                       print("{}.".format(count))
                       count=count+1
                       id.append(status.id)
                       date.append(status.created_at)
                       tweet_text.append(status.text.encode("utf-8"))
                       image_url.append(media[0]['media_url'])
                       print("Id : {}".format(status.id))
                       print("Date And Time: {}".format(status.created_at))
                       print(u"Tweet is : {} ".format(status.text).encode("utf-8"))
                       print("Image Url : {}".format(media[0]['media_url']))
                       img_url = media[0]['media_url']
                       target_path='{}/{}.jpg'.format(username,status.id)
                       profile_pic=wget.download(img_url,target_path)
                       for i in  range(len(user_mention)):
                          print("Mention Username are : {}".format(user_mention[i]['screen_name']))      
                       print("\n")               


def tweets_to_data_frame(username):
        api = tweepy.API(auth)
        tweets = api.user_timeline(screen_name=username,
                           count=20 )
        df = pd.DataFrame(data=[tweet.id for tweet in tweets], columns=['id'])
        
        df['date'] = np.array([tweet.created_at for tweet in tweets])
        df['len'] = np.array([len(tweet.text) for tweet in tweets])
        
        df['source'] = np.array([tweet.source for tweet in tweets])
        df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['Tweets'] = np.array([tweet.text.encode("utf-8").decode("utf-8") for tweet in tweets])
        return df
if __name__ == '__main__':
     def main(username):
   
               info(username)
               print("#------------------------ Media Files-----------------------------# ")
               
               twiiter_media(username)
               print("#----------------------- Tweet Records--------------------------#")
               
               
               df = tweets_to_data_frame(username)
               print(df)
               path_for_csv='{}/{}.csv'.format(username,username)
               df.to_csv(path_for_csv, index=False,encoding='utf-8')
          

  


    
          




    
  
