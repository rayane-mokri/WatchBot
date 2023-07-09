import os
import json
import datetime
import requests
import progressbar
from dotenv import load_dotenv


def reddit_connect(ID, secret, username, psswd):
    auth = requests.auth.HTTPBasicAuth(ID, secret)
    data = {"grant_type": "password",
            "username": username,
            "password": psswd}
    headers = {"User-agent": "WatchBot/0.0.1"}
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)
    token = res.json()["access_token"]
    headers = {**headers, **{'Authorization': f"bearer {token}"}}

    return headers


def reddit_retrieve_top(topics, nb_articles=5):
    darticles = {}

    load_dotenv()
    REDDIT_ID = os.getenv('REDDIT_ID')
    REDDIT_SECRET = os.getenv('REDDIT_SECRET')
    REDDIT_USERNAME = os.getenv('REDDIT_USERNAME')
    REDDIT_PSSWD = os.getenv('REDDIT_PSSWD')

    for topic in progressbar.progressbar(topics):
        articles = []
        headers = reddit_connect(REDDIT_ID, REDDIT_SECRET, REDDIT_USERNAME, REDDIT_PSSWD)
        res = requests.get(f"https://oauth.reddit.com/r/{topic}/top/?t=week", headers=headers)
        for i in range(nb_articles):
            try:
                base = res.json()["data"]["children"][i]["data"]
                article = {"tag": base["link_flair_text"],
                           "title": base["title"],
                           "url": base["url"],
                           "text": base["selftext"],
                           "link": "https://www.reddit.com" + base["permalink"],
                           "date": str(datetime.date.today())
                           }
                articles.append(article)
            except:
                pass
            darticles.update({topic: {str(datetime.date.today()): articles}})

    with open("articles.json", "w") as fp:
        json.dump(darticles, fp)

    return darticles

if __name__ == "__main__":
    reddit_retrieve_top(["MachineLearning", "coding", "python", "rust", "cpp", "unrealengine", "golang"])
