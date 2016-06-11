import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from urllib2 import urlopen
from time import gmtime, strftime

from article_polarity import *

import logging as log
log.basicConfig(filename='../info.log',level=log.WARNING)

def get_bi():

    header = {
            'User-Agent': 'Mozilla/5.0'
        }
    
    # URL of the main page that lists all articles
    url = "http://www.businessinsider.com/warroom/small-business/?r=AU&IR=T"
    # Request the page
    r = requests.get(url, headers = header)
    # Turn data into text
    data = r.text
    # Turn data into a HTML tree
    soup = BeautifulSoup(data)

    avg_pol = get_ap(soup, 'div', 'river-post', 0, pub = "bi")
    
    log.warning("Done: Business Insider " + strftime("%H:%M:%S", gmtime()))
    
    return (avg_pol)

