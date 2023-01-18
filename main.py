# You can use this script to make a tweet with python or build on it to make a Twitter Bot.
# Here is the basic code for it. Remember to set up your Twitter Dev account up to get your API tokens!!

import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# Create a tweet
api.update_status("This tweet was made by ____ with Python")
