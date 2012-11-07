from main import *
from cron_jobs.create_clusters import *
from cron_jobs.stats_cron import *

class CreateClusters(BaseHandler):
    def get(self):
        main()

class CreateData(BaseHandler):
    def get(self):
        create_data()
      
app = webapp2.WSGIApplication([('/cron/create_clusters', CreateClusters),
                               ('/cron/create_data', CreateData)
                              ], debug=True)
