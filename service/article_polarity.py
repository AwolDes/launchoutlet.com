import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from urllib2 import urlopen

# Function takes the soup object, div name, class name, number of loops until the link and the publication/blog.
def get_ap(soup, div, css_class, loops, pub = None):
    # Set the header so request is always accepted
    header = {
            'User-Agent': 'Mozilla/5.0'
        }
    # Get all divs that hold main links to articles
    if css_class != None:
        divs = soup.find_all(div, {'class':css_class})
    else:
        divs = soup.find_all(div)
    
    
    
    # Define a list for sentiments to be stored in
    sentiment = []
    for i in divs:
        # i needs to be a string, not a bs4 type to be converted into a html tree
        i = str(i)
        content = BeautifulSoup(i)
        links = []
        # To get the article Title in the following loop
        looped = 0
        for link in content.find_all('a'):
            # Using the loops parameter to get link
            if looped == loops:
                title = (link.get_text())
                #print title
            links.append(link.get('href'))
            looped += 1

        # New sets of original data points
        new_url = links[0]
        # Checks pub parameter to handle request header
        if pub == "tc":
            new_r = requests.get(new_url)
        else:
            new_r = requests.get(new_url, headers = header)
            
        new_data = new_r.text
        new_soup = BeautifulSoup(new_data)
        
        items = []
        text = ""
        # Special cases
        if pub == "bi" or "tc" or "tf" or "lh":
        
            for item in new_soup.find_all('p'):
                #print(link.get('href'))
                items.append(item.get_text())
                # the ". " makes sure sentences are correctly formed 
                text += ". " + (item.get_text())
        # What to do if it's venturebeat
        if pub == "vent":
            article = new_soup.find_all('div', {'class':'article-content'})
            
            for i in article:
                i = str(i)
                content = BeautifulSoup(i)
                for item in content.find_all('p'):
                    #print(link.get('href'))
                    items.append(item.get_text())
                    # the ". " makes sure sentences are correctly formed 
                    text += ". " + (item.get_text())
        # What to do if it's killer startups
        if pub == "ks":
            article = new_soup.find_all('article')
            for i in article:
                i = str(i)
                content = BeautifulSoup(i)
                for item in content.find_all('p'):
                    #print(link.get('href'))
                    items.append(item.get_text())
                    # the ". " makes sure sentences are correctly formed 
                    text += ". " + (item.get_text())
        
        blob = TextBlob(text)
        sentiment_of_article = title + ": " + str(blob.sentiment.polarity)
        #print sentiment_of_article
        sentiment.append(blob.sentiment.polarity)

    #print sentiment
    total = sum(sentiment)
    #print total
    avg = total/(len(sentiment))
    #print avg
    return(float(avg))
