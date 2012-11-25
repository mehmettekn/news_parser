from parsers.rssparser import RssParser

import webapp2

class HealthNewsParser(RssParser):
    def get(self):
        self.parse_rss('health_urls')
        
app = webapp2.WSGIApplication([('/health_parser', HealthNewsParser)], debug=True)
