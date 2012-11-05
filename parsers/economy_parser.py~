from rssparser import *

class EconomyNewsParser(RssParser):
    def get(self):
        self.parse_rss('economy_urls')
        
app = webapp2.WSGIApplication([('/economy_parser', EconomyNewsParser)], debug=True)
