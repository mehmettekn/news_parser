from main import *

class Channel(BaseHandler):
    def get(self):
        self.render('channel.html')

class FrontPageHandler(BaseHandler):   
    def get(self):
        posts, age = get_posts()        
        self.render('frontpage.html', posts = posts, age = age_str(age))

app = webapp2.WSGIApplication([('/', FrontPageHandler),
                               ('/channel', Channel)], debug=True)
