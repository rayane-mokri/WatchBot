import datetime
import json
import os

import progressbar
import requests
import xml.etree.ElementTree as ET


def get_arxiv_articles(topics, filename, max_results=25):
    darticles = {}
    for topic in progressbar.progressbar(topics):
        base_url = "http://export.arxiv.org/api/query?"
        query_params = {
            "search_query": topic,
            "start": 0,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending"
        }

        response = requests.get(base_url, params=query_params)
        if response.status_code != 200:
            print(f"Error: Could not fetch articles. Status code: {response.status_code}")
            return []

        articles = []
        root = ET.fromstring(response.text)

        for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
            article = {
                'title': entry.find('{http://www.w3.org/2005/Atom}title').text.strip(),
                'abstract': entry.find('{http://www.w3.org/2005/Atom}summary').text.strip(),
                'authors': [author.text.strip() for author in entry.findall('{http://www.w3.org/2005/Atom}author/\
                {http://www.w3.org/2005/Atom}name')],
                'published': entry.find('{http://www.w3.org/2005/Atom}published').text.strip(),
                'link': entry.find('{http://www.w3.org/2005/Atom}link[@title="pdf"]').attrib['href']
            }
            articles.append(article)
        darticles.update({topic: {str(datetime.date.today()): articles}})
    if not os.path.exists("../articles"):
        os.makedirs("../articles")
    with open("articles/"+ filename, "w") as fp:
        json.dump(darticles, fp, indent=4)

    return "Arxiv retrieved"


if __name__ == "__main__":
    query = ["cat:cs.LG", "cat:cs.CL", "cat:cs.ET"]   # Use the arXiv category LG - ML,
    max_results = 25
    articles = get_arxiv_articles(query, "test.json", max_results)
