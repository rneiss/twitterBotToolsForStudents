from TwitterFollowBot import TwitterBot

my_bot = TwitterBot()
#my_bot.sync_follows()

phrase = "Jewish"
count = 100
result_type = "recent"

result = my_bot.search_tweets(phrase, count, result_type)

for tweet in result["statuses"]:
    print( tweet["user"]["screen_name"] )


#my_bot.send_tweet(markov.generate_markov_text())


