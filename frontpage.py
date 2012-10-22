from main import *
from post import *

class FrontPageHandler(BaseHandler):
    def get(self):
        posts = db.GqlQuery("SELECT * FROM Post ORDER BY pubDate DESC limit 20")
        logging.error("DB QUERY!!")
        self.render('frontpage.html', posts = posts)

app = webapp2.WSGIApplication([('/', FrontPageHandler)], debug=True)
