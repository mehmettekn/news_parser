from parsers.rssparser import RssParser

import webapp2

class EconomyNewsParser(RssParser):
    def get(self):
        self.parse_rss('economy_urls')
        
app = webapp2.WSGIApplication([('/economy_parser', EconomyNewsParser)], debug=True)
