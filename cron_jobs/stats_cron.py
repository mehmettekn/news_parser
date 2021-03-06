from models.stats_data import Data, get_Query
from models.post import Post
from models.urls import urllist, srcmap
from models.tzinfo import GMT2

from google.appengine.ext import db

from datetime import datetime, timedelta

import time
import logging

increment = 10

def count_posts(newstype, srckey, hours, minutes):
    global increment    
    min2 = 0    
    if minutes > 0:
        min2 = minutes - increment    
    count = (
             get_Query(Post)._filter('newstype =', newstype)._filter('srckey =', srckey)
             ._filter('pubDate >', datetime.now(GMT2()) - timedelta(hours = hours))
             ._filter('pubDate >', datetime.now(GMT2()) - timedelta(minutes = minutes))
             ._filter('pubDate <', datetime.now(GMT2()) - timedelta(minutes = min2))
             .count(limit = None)
            )
    return count

def create_data():
    starttime = time.time()    
    global datetime, increment    
    data_batch = []
    for minute in range(0, 60, increment):    
        count = count_posts(None, None, 1, minute)
        datetime = datetime.now(GMT2()) - timedelta(minutes = minute)        
        data = Data(value = count, newstype = None,
                    src = None, datetime = datetime)
        data_batch.append(data)
        for newstype in urllist:
            count = count_posts(newstype, None, 1, minute)     
            datetime = datetime.now(GMT2()) - timedelta(minutes = minute)
            data = Data(value = count, newstype = newstype,
                        src = None, datetime = datetime)
            data_batch.append(data)
        for urlkey in srcmap:
            count = count_posts(None, urlkey, 1, minute)
            datetime = datetime.now(GMT2()) - timedelta(minutes = minute)
            data = Data(value = count, newstype = None,
                        src = srcmap[urlkey], datetime = datetime)
            data_batch.append(data)
    db.put(data_batch)
    print 'This job took to much time, around %s seconds' %(time.time() - starttime)

