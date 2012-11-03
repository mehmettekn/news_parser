
import webapp2

from parsers.economy_parser import *
from parsers.news_parser import * 
from parsers.tech_parser import *
from parsers.health_parser import * 
from parsers.sports_parser import *


app = webapp2.WSGIApplication([
    ('/parser/health_parser', HealthNewsParser),
    ('/parser/economy_parser', EconomyNewsParser),
    ('/parser/news_parser', NewsParser),
    ('/parser/sports_parser', SportsNewsParser),
    ('/parser/tech_parser', TechNewsParser)
    ], debug=True)



