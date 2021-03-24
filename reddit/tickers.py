import requests
import warnings
import random
import re

def getAllTickers():
    headers = {'User-Agent': ''.join([str(random.randint(0,9)) for i in range(10)])}
    stocks = []
    page = 1
    session = requests.Session()
    
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

        while True:
            print(page, len(stocks))
            data = session.get('https://eodhistoricaldata.com/exchange/US?page=' + str(page), headers=headers, verify=False)

            matches = re.findall('<a href="\/financial-summary\/.+">\n(.*?)\n', data.content.decode('utf-8'))
            matches = [match.replace(' ', '').split('.')[0].lower() for match in matches]

            if matches[0] in stocks:
                break

            page += 1

            with open('stocks.csv', 'a+') as f:
                f.write(',' + ','.join(matches))

            stocks += matches
