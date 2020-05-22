import tweepy
import time
auth = tweepy.OAuthHandler('cLTO6DH36ro7O2FWu69UA10hb', 'dFVOrdhSDvacenIwhkM7QzV6feKJvoyFCTGI6aq0VkiVxdxGSB')
auth.set_access_token('1246733676173393920-riiHWmpKCLukG6T224ApRTfJD6swsX', 'NCgsVw4AZX9LLmv5KbmyabuNgbVkWoXvbG4Z822f2YZOZ')
api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)
    except StopIteration:
        pass

search_string = 'python'
numberOfTweets = 2
for tweet in tweepy.Cursor(api.search,search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        print("liked the tweet")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


#generous bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == "rishitha":
#         follower.follow()
#         print(follower.name)

