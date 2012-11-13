from parsers import feedparser
import json
    
url = "http://www.haberturk.com/rss/manset.xml"

def generate_json():
    json = dict()
    json['Posts'] = []
    xml = feedparser.parse(url)

    posts = xml["entries"]
    for post in posts:
        json['Posts'].append({
                'Title':post['title'],
                'Link': post['link'],
                'pubDate':post['published_parsed']
                })

    return json

             

