import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from urllib2 import urlopen
from time import gmtime, strftime

from article_polarity import *

import logging as log
log.basicConfig(filename='../info.log',level=log.WARNING)

def get_tf():
     header = {
            'User-Agent': 'Mozilla/5.0'
        }
    
     # URL of the main page that lists all articles
     url = "http://startups.techfact.org/"
     # Request the page
     r = requests.get(url, headers = header)
     # Turn data into text
     data = r.text
     # Turn data into a HTML tree
     soup = BeautifulSoup(data)

     avg_pol = get_ap(soup, 'article', None, 0, pub = "tf")
     
     log.warning("Done: TechFact " + strftime("%H:%M:%S", gmtime()))
     
     return (avg_pol)
