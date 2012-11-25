from parsers.rssparser import RssParser

import webapp2

class TechNewsParser(RssParser):
    def get(self):
        self.parse_rss('tech_urls')
        
app = webapp2.WSGIApplication([('/tech_parser', TechNewsParser)], debug=True)
