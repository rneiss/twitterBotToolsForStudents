from TwitterFollowBot import TwitterBot
import random

my_bot = TwitterBot()
#my_bot.sync_follows()

file_ = open('TwitterBot/tanach.txt')
randomLine = (random.choice(list(file_)))

my_bot.send_tweet(randomLine)


