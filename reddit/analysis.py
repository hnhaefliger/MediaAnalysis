import requests
import warnings
import enchant
import re
import random

def onYahooFinance(ticker):
    '''
    Check if a symbol is on yahoo finance.
    '''
    headers = {'User-Agent': ''.join([str(random.randint(0,9)) for i in range(10)])}

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

        response = requests.get('https://query1.finance.yahoo.com/v7/finance/download/' + ticker, verify=False, headers=headers, stream=True)

    return response.status_code == 200

def isNotEnglish(word):
    '''
    Check if a word is not in the english language.
    '''
    dictionary = enchant.Dict("en_US")
    
    return not(dictionary.check(word))
    
def isTicker(word):
    '''
    Check if a word is in the english dictionary. 
    '''
    return isNotEnglish(ticker) and onYahooFinance(ticker)

def countMentions(post):
    '''
    Count the mentions of different tickers in a text.
    '''
    regex = re.compile("[^a-zA-Z' ]")
    text = post['text']
    text = text.replace('/', '')
    text = regex.sub('', text)

    stocks = []

    for word in text.split(' '):
        if isTicker(word):
            stocks.append(word.upper())

    return stocks
