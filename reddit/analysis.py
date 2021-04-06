import requests
import warnings
import re
import random
import os
import numpy as np
import time

with open(os.path.dirname(os.path.abspath(__file__)) + '/stocks.csv', 'r') as f:
    tickers = f.read().split(',')

START = int(time.time())

def sigmoid(x):
    '''
    Sigmoid / Logistic function.
    '''
    return 1 / (1 + np.exp(x))

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

def score(post):
    '''
    Asigm a score between 1 and 0 to a given post.
    '''
    upvote_ratio = 0
    
    if post['ups'] > 0:
        upvote_ratio = post['ups'] / (post['ups'] + post['downs'])
        
    views = 1
    time_since = 1 - sigmoid((START - int(post['created_utc'])) / 1e8 * 12 - 6)
    length = sigmoid(len(post['text']) * 12 / 5000 - 6)

    return upvote_ratio * views * length * time_since
    
