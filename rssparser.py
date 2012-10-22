from main import *
from bs4 import BeautifulSoup
from google.appengine.api import urlfetch
from xml.dom import minidom
from collections import namedtuple
from time import strptime, mktime
from datetime import datetime
from dateutil import parser

urllist = {"http://www.haberturk.com/rss":{}, 
           "http://www.milliyet.com.tr/D/rss/rss/RssSD.xml":{},
           "http://rss.hurriyet.com.tr/rss.aspx?sectionId=1":{},
           "http://www.sabah.com.tr/rss/SonDakika.xml":{},
           "http://www.radikal.com.tr/d/rss/RssSD.xml":{}}

no_image_url = "https://encrypted-tbn1.gstatic.com/images?      q=tbn:ANd9GcTEzsZdA0I-mk9lPYUZaJbJ6rcTYXl53Rv1uin78SRlckU9MwV6Kw"

class RssParser(BaseHandler):
    def get_data(self, name, src):
        _data = src.getElementsByTagName(name)[0]
        data = _data.lastChild.data
        return data    

    def parse_rss(self):
        result = namedtuple('Result', ['title', 'description', 'link',
                                   'content', 'image', 'pubDate', 'src'])
        results = []
        for url in urllist:
            page = urlfetch.fetch(url).content
            xml = minidom.parseString(page)
            posts = xml.getElementsByTagName("item")
            source = self.get_data("title", xml)            
            for post in posts:
                title = self.get_data("title", post)
                _desc = BeautifulSoup(self.get_data("description", post))
                desc = _desc.get_text()
                link = self.get_data("link", post)
                _image = _desc.find('img')
                _pubDate = self.get_data('pubDate', post)
                pubDate = parser.parse(_pubDate)             
                if _image: image = _image['src']
                else: image = no_image_url
                content = "no content yet" #add parsing for content later"
                src = source      
                results.append(result(title, desc, link, content, image, pubDate, src))
        return results 
            
 
