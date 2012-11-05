from parsers.rssparser import *

class SportsNewsParser(RssParser):
    def get(self):
        self.parse_rss('sports_urls')
        
app = webapp2.WSGIApplication([('/sports_parser', SportsNewsParser)], debug=True)
