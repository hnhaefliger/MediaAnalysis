from reddit import *

def getStocks(subreddit, ranking, limit):
    '''
    Get a list of highest scoring stocks on a subreddit.
    '''
    data = getPosts(subreddit, ranking, limit)

    stocks = {}

    for post in data:
        for stock in countMentions(post):
            if stock in stocks:
                stocks[stock] += 1

            else:
                stocks[stock] = 1

    return stocks
