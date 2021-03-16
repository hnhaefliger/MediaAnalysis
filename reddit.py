import requests
import random
import json
import numpy as np

def gradePost(post):
    '''
    useful fields:
        kind,
        data.title,
        data.selftext,
        data.downs,
        data.upvote_ratio,
        data.ups,
        data.total_awards_received,
        data.score,
        data.num_comments,
        data.subreddit_subscribers,
    
    potentially useful fields: 
        data.gilded,
        data.link_flair_text,
        data.top_awarded_type,
        data.is_original_content,
        data.category,
        data.author_premium,
        data.gildings,
        data.content_categories,
        data.created,
        data.allow_live_comments,
        data.suggested_sort,
    '''
    metrics = np.array([
                        post['downs'],
                        post['ups'],
                        post['upvote_ratio'],
                        post['total_awards_received'],
                        post['score'],
                        post['num_comments'],
                        post['subreddit_subscribers'],
                        ])
    weights = np.array([
                        0,
                        0,
                        0,
                        0,
                        1e-4,
                        0,
                        0,
                        ])
    return np.dot(weights.T, metrics)

def evaluatePost(post):
    mentions = countMentions(post)
    score = gradePost(post)
    return score

def getPosts(subreddit='wallstreetbets', endpoint='top', limit=100):
    headers = {'User-Agent': ''.join([str(random.randint(0,9)) for i in range(10)])}
    response = requests.get('https://www.reddit.com/r/' + subreddit + '/' + endpoint + '/.json?limit=' + str(limit), headers=headers)

    return response.json()
