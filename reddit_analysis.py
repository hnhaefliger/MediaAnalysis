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
            score = reddit.score(post)
            if stock in stocks:
                stocks[stock] += score

            else:
                stocks[stock] = score

    dictionary = enchant.Dict("en_US")
    cleanstocks = {}
    
    for stock in stocks.keys():
        if not(dictionary.check(stock)):
            cleanstocks[stock] = stocks[stock]

    return cleanstocks


def getSubs(subreddits, ranking, n_posts):
    '''
    Total mentions from several subreddits.
    '''
    stocks = {}

    for subreddit in subreddits:
        found = getStocks(subreddit, ranking, n_posts)
        for stock in found:
            if stock in stocks:
                stocks[stock] += found[stock]

            else:
                stocks[stock] = found[stock]

    return stocks

def getTopStocks(n_stocks, n_posts):
    stocks = getSubs([
                    'pennystock',
                    'pennystocks',
                    'pennystocksdd',
                    'pennycatalysts',
                    'robinhoodpennystocks',
                    'pennyhaven',
                    'pennygains',
                    'pennydd',
    ], 'rising', n_posts)
    
    stocks = {k: v for k, v in sorted(stocks.items(), key=lambda item: -item[1])}

    i = 0
    for stock in stocks:
        i += 1
        if i > n_stocks:
            break

        print(stock, ':', stocks[stock])
