from stats import crons,ajax,generate,mainh

import webapp2



app = webapp2.WSGIApplication([
	('/', mainh.MainHandler),
	('/crons/5min/', crons.FiveMinHandler),
	('/crons/1day/', crons.OncePerDayHandler),
	('/ajax/24hours/', ajax.TwentyFourHours),
	('/ajax/7days/', ajax.SevenDays),
	('/ajax/30days/', ajax.ThirtyDays),
	('/generate-test-data/', generate.GenerateTestData)
],debug=True)



#app = webapp2.WSGIApplication([('/create_clusters', CreateClusters)], debug=True)
