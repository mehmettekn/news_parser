from main import *
from stats.data_generator import generate_data

class Main(BaseHandler):
    def get(self):
        self.render('stats.html')

class LastHour(BaseHandler):
    def get(self):
        json_str= generate_data(days = 0, minutes = 60)
        self.write(json_str)
        
class LastSixHours(BaseHandler):
    def get(self):
        json_str = generate_data(days = 0, minutes = 360)
        self.write(json_str)

class LastTwelveHours(BaseHandler):
    def get(self):
        json_str = generate_data(days = 0, minutes = 720)
        self.write(json_str)

class TwentyFourHours(BaseHandler):
    def get(self):
        json_str = generate_data(days = 1, minutes = 0)
        self.write(json_str)

class SevenDays(BaseHandler):
    def get(self):
        json_str = generate_data(days = 7, minutes = 0)
        self.write(json_str)

class ThirtyDays(BaseHandler):
    def get(self):
        json_str = generate_data(days = 30, minutes = 0)
        self.write(json_str)

app = webapp2.WSGIApplication([
        ('/stats/lasthour/', LastHour),
        ('/stats/last6hours/', LastSixHours),
        ('/stats/last12hours/', LastTwelveHours),
        ('/stats/24hours/', TwentyFourHours),        
        ('/stats/7days/', SevenDays),
        ('/stats/30days/', ThirtyDays),
        ('/stats', Main)
        ], debug = True)

