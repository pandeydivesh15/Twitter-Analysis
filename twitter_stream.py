#Neccessory imports
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream

#Set up user credentials to access Twitter API
ACCESS_TOKEN = "Your value"
ACCESS_TOKEN_SECRET = "Your value"
CONSUMER_KEY = "Your value"
CONSUMER_SECRET = "Your value"

#Listener object
class StdOutListener(StreamListener):

    def on_data(self, data):
        """Just prints out incoming data to the stdout"""
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':

    #Handles Twitter authentification and the connection to Twitter Streaming API.
    l = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    stream = Stream(auth, l)

    #Filter the tweets according to your requirements. Set a basis for which data to capture.
    stream.filter(track=['#epl', '#bpl'])