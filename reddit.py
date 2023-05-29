import os
import requests
from dotenv import load_dotenv


def reddit_connect(ID, SECRET, USERNAME, PSSWD):
    auth = requests.auth.HTTPBasicAuth(ID, SECRET)
    data = {'grant_type': 'password',
            'username': USERNAME,
            'password': PSSWD}
    headers = {'User-Agent': 'MyBot/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)
    TOKEN = res.json()['access_token']
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
    return headers


def reddit_retrieve_top(topics, REDDIT_ID, REDDIT_SECRET, REDDIT_USERNAME, REDDIT_PSSWD):
    darticles = {}
    for topic in topics :
        articles = []
    
        headers = reddit_connect(REDDIT_ID, REDDIT_SECRET, REDDIT_USERNAME,
                                REDDIT_PSSWD)
        requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)
        res = requests.get(f"https://oauth.reddit.com/r/{topic}/top/?t=week",
                        headers=headers)
        for i in range(5):
            base = res.json()["data"]["children"][i]["data"]
            article = {"tag": base["link_flair_text"],
                    "title": base["title"],
                    "url": base["url"],
                    "text":base["selftext"],
                    "link": "https://www.reddit.com" + base["permalink"]
                    }
            articles.append(article)
        darticles.update({topic : articles})
    return darticles 