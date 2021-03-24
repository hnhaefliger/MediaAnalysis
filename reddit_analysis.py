import reddit
import enchant

def getStocks(subreddit, ranking, limit):
    '''
    Get a list of highest scoring stocks on a subreddit.
    '''
    data = reddit.getPosts(subreddit, ranking, limit)

    stocks = {}

    for post in data:
        for stock in reddit.countMentions(post):
            if stock in stocks:
                stocks[stock] += 1

            else:
                stocks[stock] = 1

    dictionary = enchant.Dict("en_US")
    cleanstocks = {}
    
    for stock in stocks.keys():
        if not(dictionary.check(stock)):
            cleanstocks[stock] = stocks[stock]

    return cleanstocks
