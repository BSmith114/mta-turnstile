'''Pull links and build postgres db '''
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs
import requests as r

def mta_turnstile_web_scrape():
    """
    :param: no params
    :return: list of links from mta turnstile date website
    """
    url = "http://web.mta.info/developers/turnstile.html"
    data_url = "http://web.mta.info/developers/"
    html = r.get(url)
    soup = bs(html.content, 'lxml')
    links = [urljoin(data_url, link.attrs['href']) for link in soup.select('.span-84 a')]
    return links

