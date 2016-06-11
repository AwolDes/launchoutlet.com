from tc import *
from vent import *
from biz import *
from tf import *
from lh import *
from ks import *

from html import *

from bubble import *

from time import gmtime, strftime

wipe = open("../info.log", "r+")
wipe.seek(0)
wipe.truncate()
wipe.close()

import logging as log
log.basicConfig(filename='../info.log',filemode='w',level=log.WARNING)
### IDEAS ###

### Sentiment of titles
### History of senitment and how it changes
## Sentiment of large launches
## Number of mentions of the startup (?)
### Amount of articles posted a day
## Nicest Journlists at respective blogs -> sell warm intros
## Social shares; which platform shares most, and correlation between sentiment
#  and amount of shares.

###### Then work ($$$$) with startups on launch day to find users sharing the article and create a list

log.warning("Starting now " + strftime("%H:%M:%S", gmtime()))


tc = get_tc()
vent = get_vent()
bi = get_bi()
tf = get_tf()
lh = get_lh()
ks = get_ks()
#mash = get_mash()

srcs = [tc, vent, bi, tf, lh, ks]
#print srcs

srcs = bubble(srcs)
#print srcs
src_names = []
## Match them with their urls
for i in srcs:
    if i == tc:                                    
        src_names.append(["http://techcrunch.com/startups/","TechCrunch"])
    elif i == vent:
        src_names.append(["http://venturebeat.com/category/small-biz/","VentureBeat"])
    elif i == bi:
        src_names.append(["http://www.businessinsider.com/warroom/small-business/?r=AU&IR=T","Business Insider"])
    elif i == tf:
        src_names.append(["http://startups.techfact.org/","TechFact"])
    elif i == lh:
        src_names.append(["http://www.lifehacker.com.au/work/small-business-startups/","Life Hacker"])
    elif i == ks:
        src_names.append(["http://killerstartups.com/startup-reviews/","Killer Startups"])
#print src_names

gen_html(src_names)


log.warning("All Done :) " + strftime("%H:%M:%S", gmtime()))


    






