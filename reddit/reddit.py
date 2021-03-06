import requests
import random
import json
import warnings

def cleanPost(post):
    '''
    Remove useless fields from a post.
    '''
    clean_post = {}

    if 'selftext' in post: clean_post['text'] = post['title'] + '. ' + post['selftext']
    else: clean_post['text'] = post['body']

    clean_post['score'] = post['score']
    clean_post['ups'] = post['ups']
    clean_post['downs'] = post['downs']
    clean_post['id'] = post['id']
    clean_post['created_utc'] = post['created_utc']

    if 'depth' in post: clean_post['depth'] = post['depth'] + 1
    else: clean_post['depth'] = 0

    return clean_post

def extractComments(tree):
    '''
    Get all comments from a comments tree.
    '''

    try:
        if tree['replies']:
            return [cleanPost(tree)] + [extractComments(child['data'])[0] for child in tree['replies']['data']['children'] if 'body' in child['data']]

        else:
            return [cleanPost(tree)]

    except:
        return [{
                'text': '',
                'score': 0,
                'ups': 0,
                'downs': 0,
                'id': 0,
                'depth': 0,
                'created_utc': 0,
            }]

def getComments(subreddit, post):
    '''
    Get all comments on a post.
    '''
    headers = {'User-Agent': ''.join([str(random.randint(0,9)) for i in range(10)])}

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        response = requests.get('https://www.reddit.com/r/' + subreddit + '/comments/' + post + '.json?limit=100000', headers=headers, verify=False)

    data = response.json()[1]['data']['children']

    comments = []

    for comment in data:
        comments += extractComments(comment['data'])

    return comments
    
def getPosts(subreddit, ranking, limit):
    '''
    Get all posts from a subreddit.
    '''
    headers = {'User-Agent': ''.join([str(random.randint(0,9)) for i in range(10)])}

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        response = requests.get('https://www.reddit.com/r/' + subreddit + '/' + ranking + '/.json?limit=' + str(limit), headers=headers, verify=False)

    data = response.json()['data']['children']
    data = [cleanPost(post['data']) for post in data]
    all_data = list(data)

    for post in data:
        all_data += getComments(subreddit, post['id'])

    return all_data
