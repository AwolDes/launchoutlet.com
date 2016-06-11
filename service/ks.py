import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from urllib2 import urlopen
from time import gmtime, strftime

from article_polarity import *

import logging as log
log.basicConfig(filename='../info.log',level=log.WARNING)
## Scrape the second page as well (/page/2/)
def get_ks():
     header = {
            'User-Agent': 'Mozilla/5.0'
        }
    
     # URL of the main page that lists all articles
     url = "http://killerstartups.com/startup-reviews/"
     # Request the page
     r = requests.get(url, headers = header)
     # Turn data into text
     data = r.text
     # Turn data into a HTML tree
     soup = BeautifulSoup(data)
    
     avg_pol = get_ap(soup, 'div', "et-description", 0, pub = "ks")
     
     log.warning("Done: Killer Startups " + strftime("%H:%M:%S", gmtime()))
     
     return (avg_pol)


