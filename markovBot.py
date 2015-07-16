from TwitterFollowBot import TwitterBot
import markovgen

my_bot = TwitterBot()
#my_bot.sync_follows()

file_ = open('TwitterBot/tanach.txt')
markov = markovgen.Markov(file_)

my_bot.send_tweet(markov.generate_markov_text())


