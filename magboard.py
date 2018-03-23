import tweepy
import json
import re

# Specify the account credentials in the following variables:
consumer_key = 'No3XJW8ccIOtCRsF4LXGENziy'
consumer_secret = 'LMN57iFjDOVC165rZY0bqwZDLyWqXU0dlmp2eo34jCccbMzgYq'
access_token = '838112658-iwEy6pxUEWNXjfCsolJhgHx02uOhUOzKCfskt4tI'
access_token_secret = 'lOCyySzJwipR8mV1IwpZ6WvbQDoAMeZVQBR6LhpWrB5i8'


# This listener will print out all Tweets it receives
list_array =[]
file = open('tweets.txt', 'a')
class PrintListener(tweepy.StreamListener):
    def on_data(self, data):
        # Decode the JSON data
        tweet = json.loads(data)

        # Print out the Tweet
        tweet_filter = str(tweet['text'].encode('ascii', 'ignore'))
        tweet_text = tweet_filter.replace("RT", '')
        list_array.append(tweet_filter)
        print(len(list_array))
        file.write(tweet_text+'\n')



    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    listener = PrintListener()

    # Show system message
    print('I will now print Tweets containing "Padmavati"! ==>')

    # Authenticate
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Connect the stream to our listener
    stream = tweepy.Stream(auth, listener)
    stream.filter(track=['padmavati', '#padmavati'])