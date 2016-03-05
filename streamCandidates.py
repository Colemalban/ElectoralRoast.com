from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import unicodedata


ckey = '9QNHTvlJIUm6nW0xZfCQrbv1c'
csecret = 'H8poLEFkwNM0PoBxSvzHsF0c3l3PJEUI8DPvEJnWuKQOCw5BRJ'
atoken = '199110460-MbCtBAwLlxDd54qiV73uebJglTPTfAYZ6Z8zDCYo'
asecret = 'MNLqjreqgEwihGYgqkvexJ0JZlgNbAltfyfuwDHaOyPMX'
trump = open("trump.txt", "w")
clinton = open("clinton.txt", "w")
bernie = open("bernie.txt", "w")
rubio = open("rubio.txt", "w")
cruz = open("cruz.txt", "w")
class listener(StreamListener):
	def on_data(self, data):
		decoded = json.loads(str(data))
		if 'place' in decoded and decoded['place'] is not None:
			loc = decoded['place']['bounding_box']['coordinates'][0][0]
			tweet = str(decoded['text'].encode("unicode_escape"))
			tweet = tweet[1:]
			tweetLower = tweet.lower()
			if("trump" in tweetLower):
				trump.write('{"tweet": ' + tweet +', "coordinates": ' + str(loc) + '"}\n')
			if("sanders" in tweetLower or "bernie" in tweet.lower()):
				bernie.write('{"tweet": ' + tweet +', "coordinates": ' + str(loc) + '"}\n')
			if("clinton" in tweetLower):
				clinton.write('{"tweet": ' + tweet +', "coordinates": ' + str(loc) + '"}\n')
			if("rubio" in tweetLower):
				rubio.write('{"tweet": ' + tweet +', "coordinates": ' + str(loc) + '"}\n')
			if("cruz" in tweetLower):
				cruz.write('{"tweet": ' + tweet +', "coordinates": ' + str(loc) + '"}\n')
		return True
	def on_error(self, status):
		print (status)
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track={"Trump", "Sanders", "Bernie", "Clinton", "Rubio", "Cruz"})