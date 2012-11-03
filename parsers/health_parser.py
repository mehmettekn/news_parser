from rssparser import *

class HealthNewsParser(RssParser):
    def get(self):
        self.parse_rss('health_urls')
        
app = webapp2.WSGIApplication([('/health_parser', HealthNewsParser)], debug=True)
