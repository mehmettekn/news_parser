from parsers.rssparser import *

class TechNewsParser(RssParser):
    def get(self):
        self.parse_rss('tech_urls')
        
app = webapp2.WSGIApplication([('/tech_parser', TechNewsParser)], debug=True)
