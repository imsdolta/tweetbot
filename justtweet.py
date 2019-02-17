import tweepy, time, sys
from  credentials import keys
 
argfile = str(sys.argv[1]) # You will need to pass a .txt file as an argument in order to assign this.
 
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

# Set up OAuth - log into the account.
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
 
filename=open(argfile,'r')
f=filename.readlines() # Read the lines of the file one-by-one 
filename.close()
 
for line in f:
    api.update_status(status=line)
    time.sleep(500) 
