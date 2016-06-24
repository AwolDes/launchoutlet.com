# TechCrunch
from tc import *
# VentureBeat
from vent import *
# Business Insider
from biz import *
# Tech Fact
from tf import *
# Life Hacker
from lh import *
# Killer Startups
from ks import *

from html import *

from bubble import *

from time import gmtime, strftime



tc = get_tc()
vent = get_vent()
bi = get_bi()
tf = get_tf()
lh = get_lh()
ks = get_ks()

srcs = [tc, vent, bi, tf, lh, ks]

srcs = bubble(srcs)

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




    






