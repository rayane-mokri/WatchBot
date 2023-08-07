import json
import requests
import xml.etree.ElementTree as ET


def get_arxiv_articles(query, max_results=25):
    base_url = "http://export.arxiv.org/api/query?"
    query_params = {
        "search_query": query,
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

    return articles


if __name__ == "__main__":
    query = "cat:cs.LG"  # Use the arXiv category for machine learning
    max_results = 25
    articles = get_arxiv_articles(query, max_results)

    # Convert the articles to JSON and print the result
    json_articles = json.dumps(articles, indent=2)
    print(json_articles)
