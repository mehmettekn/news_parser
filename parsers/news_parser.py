from parsers.rssparser import RssParser

import webapp2

class NewsParser(RssParser):
    def get(self):
        self.parse_rss('news_urls')

app = webapp2.WSGIApplication([('/news_parser', NewsParser)], debug=True)
