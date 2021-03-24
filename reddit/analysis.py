import requests
import warnings
import enchant
import re
import random

with open('stocks.csv', 'r') as f:
    tickers = f.read().split(',')

def onYahooFinance(ticker):
    '''
    Check if a symbol is on yahoo finance.
    '''
    return ticker in tickers

def isNotEnglish(word):
    '''
    Check if a word is not in the english language.
    '''
    dictionary = enchant.Dict("en_US")
    
    return not(dictionary.check(word))
    
def isTicker(ticker):
    '''
    Check if a word is in the english dictionary. 
    '''
    if len(ticker) > 0:
        if isNotEnglish(ticker):
            return onYahooFinance(ticker)

    else:
        return False

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
