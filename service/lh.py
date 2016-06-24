import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from urllib2 import urlopen
from time import gmtime, strftime

from article_polarity import *

def get_lh():
    # Set header for original Reuqest
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
    # Call article_polarity.py
    avg_pol = get_ap(soup, 'a', "tracking_loop_headline", 0, pub = "lh")
     
    
    return (avg_pol)
  
