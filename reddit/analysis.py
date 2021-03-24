import requests
import warnings
import re
import random
import os

with open(os.path.dirname(os.path.abspath(__file__)) + '/stocks.csv', 'r') as f:
    tickers = f.read().split(',')

def onYahooFinance(ticker):
    '''
    Check if a symbol is on yahoo finance.
    '''
    return ticker in tickers
    
def isTicker(ticker):
    '''
    Check if a word is in the english dictionary. 
    '''
    if len(ticker) > 0:
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
    text = regex.sub(' ', text)

    stocks = []

    for word in text.split(' '):
        if isTicker(word.lower()):
            stocks.append(word.upper())

    return stocks
