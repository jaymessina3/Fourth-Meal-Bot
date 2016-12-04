from twython import Twython

app_key = "Loge6bT8EBK0HK2TcMtDCy1Bg"
app_secret = "H9F6OHt0LpLlBhV7NoeCOrBnb06mntNi9lJ57dxk5Q9KjZrT3S"
oauth_token = "805092925151571968-fefc4kuHjllJnfCJiU8OLV2lGOCydIS"
oauth_token_secret =  "It9WTfWGMSF1oSRFxcjiL8SGkiGaENch5hGAkjFz3tL3q"

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)


##search_results = twitter.search(q="#fourthmeal", count=10)
##try:
##    for tweet in search_results["statuses"]:
##        twitter.retweet(id = tweet["id_str"])
##        twitter.create_favorite(id = tweet["id_str"])
##except Exception as e:
##    print (e)

search_results = twitter.search(q="#oberlinfourthmeal", count=10)
try:
    for tweet in search_results["statuses"]:
        twitter.retweet(id = tweet["id_str"])
        twitter.create_favorite(id = tweet["id_str"])
except Exception as e:
    print (e)

search_results = twitter.search(q="#oberlin", count=10)
try:
    for tweet in search_results["statuses"]:
        twitter.retweet(id = tweet["id_str"])
        twitter.create_favorite(id = tweet["id_str"])
except Exception as e:
    print (e)

search_results = twitter.search(q="#dascombfourthmeal", count=10)
try:
    for tweet in search_results["statuses"]:
        twitter.retweet(id = tweet["id_str"])
        twitter.create_favorite(id = tweet["id_str"])
except Exception as e:
    print (e)

search_results = twitter.search(q="#somanyclappingemojis", count=10)
try:
    for tweet in search_results["statuses"]:
        twitter.retweet(id = tweet["id_str"])
        twitter.create_favorite(id = tweet["id_str"])
except Exception as e:
    print (e)
