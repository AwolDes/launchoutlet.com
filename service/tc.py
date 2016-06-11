import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from urllib2 import urlopen
from time import gmtime, strftime

from article_polarity import *

import logging as log
log.basicConfig(filename='../info.log',level=log.WARNING)

def get_tc():
    # URL of the main page that lists all articles
    url = "http://techcrunch.com/startups/"
    # Request the page
    r = requests.get(url)
    # Turn data into text
    data = r.text
    # Turn data into a HTML tree
    soup = BeautifulSoup(data)

    #FOR TECH CRUNCH 
    avg_pol = get_ap(soup, 'div', 'block-content', 1, pub = "tc")
    
    log.warning("Done: TechCrunch " + strftime("%H:%M:%S", gmtime()))
    
    return (avg_pol)
  
