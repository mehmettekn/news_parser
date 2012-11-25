from models.post import get_posts, Post
from models.urls import urllist
from main import age_set, age_get

from google.appengine.ext import db

import json
import logging

def generate_posts_json(update = False):
    mc_key = "JSON_POSTS"
    news_dict, age = age_get(mc_key)
    if update or news_dict is None:     
        q = Post.all().order('-pubDate')       
        posts = list(q.fetch(limit=20))
        news_dict = dict()    
        for newstype in urllist:
            news_dict[newstype] = []            
        news_dict["carousel_posts"] = []        
        for p in posts:
            news_dict[p.newstype].append({
                    "TITLE":p.title,
                    "DESCRIPTION":p.description,
                    "PUBDATE":p.pubDate.isoformat(),
                    "LINK":p.link,
                    "IMAGE":p.image,
                    "SRC":p.src,
                    "NEWSTYPE":p.newstype #remove later
                    })
        carousel_posts = list(q.filter('srckey IN', [1, 6, 10]).fetch(limit=6))
        for p in carousel_posts:
            news_dict["carousel_posts"].append({
                    "TITLE":p.title,
                    "DESCRIPTION":p.description,
                    "PUBDATE":p.pubDate.strftime("%X, %x"),
                    "LINK":p.link,
                    "IMAGE":p.image,
                    "SRC":p.src,
                    "NEWSTYPE":p.newstype #remove later
                    })
        news_dict = json.dumps(news_dict)
        age_set(mc_key, news_dict)
        logging.info("DB QUERY!!")  
    return news_dict, age    
    
    
