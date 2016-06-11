import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from urllib2 import urlopen
from time import gmtime, strftime

from article_polarity import *
import logging as log
log.basicConfig(filename='../info.log',level=log.WARNING)
## Look into pagination
# http://stackoverflow.com/questions/29006848/scrape-data-from-paginated-contents
def get_lh():
     header = {
            'User-Agent': 'Mozilla/5.0'
        }
    
     # URL of the main page that lists all articles
     url = "http://www.lifehacker.com.au/work/small-business-startups/"
     # Request the page
     r = requests.get(url, headers = header)
     # Turn data into text
     data = r.text
     # Turn data into a HTML tree
     soup = BeautifulSoup(data)

     avg_pol = get_ap(soup, 'a', "tracking_loop_headline", 0, pub = "lh")
     
     log.warning("Done: Life Hacker " + strftime("%H:%M:%S", gmtime()))
     
     return (avg_pol)
  
