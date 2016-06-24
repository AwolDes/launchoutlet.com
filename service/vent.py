import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from urllib2 import urlopen
from time import gmtime, strftime

from article_polarity import *

import logging as log
log.basicConfig(filename='../info.log',level=log.WARNING)

def get_vent():
    # Sent user agent to avoid 403 forbidden
    header = {
            'User-Agent': 'Mozilla/5.0'
        }
    # URL of the main page that lists all articles
    url = "http://venturebeat.com/category/small-biz/"
    # Request the page with headers
    r = requests.get(url, headers = header)
    # Turn data into text
    data = r.text
    # Turn data into a HTML tree
    soup = BeautifulSoup(data)
    
    # Call article_polarity.py
    avg_pol = get_ap(soup, 'article', None, 1, pub="vent")
    
    return (avg_pol)


