import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date


def get_html_page(url):
    news_request = requests.get(url)
    if news_request.status_code == 200:
        return news_request.text
    else:
        print('Oops! Something went wrong...')
        return 0


def find_articles(html_page):
    parsed_page = BeautifulSoup(html_page, features='html.parser')
    headers = []
    for t in parsed_page.findAll('h4'):
        headers.append(t.string)
    return headers

def publish_report(path, headers):
    now = datetime.now()
    articles = [{'title': i} for i in headers]
    artjson = {'url': 'https://sobesednik.ru/psychology', 'creation Date': '{0}'.format(now.date()),
               'articles': articles}
    with open(path, "w") as write_file:
        json.dump(artjson, write_file)
    return artjson
