import tweepy
import time
import sys

class TwitterAPI:
    def __init__(self):
        consumer_key = "Loge6bT8EBK0HK2TcMtDCy1Bg"
        consumer_secret = "H9F6OHt0LpLlBhV7NoeCOrBnb06mntNi9lJ57dxk5Q9KjZrT3S"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "805092925151571968-fefc4kuHjllJnfCJiU8OLV2lGOCydIS"
        access_token_secret = "It9WTfWGMSF1oSRFxcjiL8SGkiGaENch5hGAkjFz3tL3q"
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)

if __name__ == "__main__":
          filename=open("twitterBot.txt",'r')
          f=filename.readlines()
          filename.close()
 
          for line in f:
              twitter = TwitterAPI()
              L = str(line)
              splitting = L.split()
              newL = ""
              for x in splitting:
                        newL += x
                        newL+= " \U0001F44F"                       
              twitter.tweet(newL)
              time.sleep(120)#Tweet every 24 hours = 86400 
          
