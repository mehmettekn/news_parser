from rssparser import *
from google.appengine.ext import db

def post_key(name = 'default'):
    return db.Key.from_path('posts', name)

class Post(db.Model):
    title = db.TextProperty(required = True)
    description = db.TextProperty(required = True)
    pubDate = db.DateTimeProperty(required = True)
    link = db.TextProperty(required = True)
    content = db.BlobProperty()
    image = db.LinkProperty()
    src = db.StringProperty(required = True)    
    
    def render(self):
        return render_str("post.html", p = self)


links = {}

class ParseRSS(RssParser):
    def get(self):
        results = self.parse_rss()        
        for r in results:
            if r.link not in links:            
                logging.error("New Post Entity Being Created")                
                p = Post(parent = post_key(), title = r.title,
                         description = r.description,
                         link = r.link, content = r.content,
                         image = r.image, pubDate = r.pubDate,
                         src = r.src)
                p.put()
                links[r.link] = True

app = webapp2.WSGIApplication([('/parser', ParseRSS)], debug=True)
