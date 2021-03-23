from . import reddit
from . import analysis

def getStocks(subreddit, ranking, limit):
    data = reddit.getPosts(subreddit, ranking, limit)

    stocks = {}

    for post in data:
        for stock in analysis.countMentions(post):
            if stock in stocks:
                stocks[stock] += 1

            else:
                stocks[stock] = 1

    return stocks
