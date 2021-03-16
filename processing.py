def multiIndexList(array, substring):
    occurrences = []

    while True:
        try:
            occurrence = array.index(substring)
            occurrences.append(occurrence)
            array = array[occurrence + 1:]

        except:
            break

    return occurrences

def multiIndexString(string, substring):
    occurrences = []

    while True:
        try:
            occurrence = string.index(substring)
            occurrences.append(occurrence)
            string = string[occurrence + len(substring) + 1:]

        except:
            break

    return occurences

def countMentions(post):
    text = post['title'] + '. ' + post['selftext']
    print(text)

def splitResponse(response):
    posts = []
    data = response.json()

    for child in response.json()['data']['children']:
        posts.append(evaluatePost(child['data']))

    return posts
