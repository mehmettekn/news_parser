from parsers.rssparser import RssParser

import webapp2

class SportsNewsParser(RssParser):
    def get(self):
        self.parse_rss('sports_urls')
        
app = webapp2.WSGIApplication([('/sports_parser', SportsNewsParser)], debug=True)
