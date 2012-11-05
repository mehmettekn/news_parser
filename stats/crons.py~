#!/usr/bin/env python

import time
from datetime import datetime,timedelta
from google.appengine.api import urlfetch
from google.appengine.ext import webapp,db

from models.models import *
from config import config

# The cron controllers:

class FiveMinHandler(webapp.RequestHandler):

	# Executed every five minutes, and fetches
	# Tutorialzine's homepage, while recording
	# the response time.

	def get(self):
		start = time.time()
	
		try:
			# Using appengine's URLFetch module:
			
			result = urlfetch.fetch(
						config.fetchURL,
						deadline=10,
						headers={'Cache-Control' : 'max-age=0'}
					)
									
			if result.status_code == 200 and result.content.find(config.searchString) != -1:
			
				# Saving the Ping to the datastore with the put() method.
				Ping(responseTime = int((time.time() - start)*1000)).put()
				self.response.out.write("OK!")
			else:
				raise Exception('This website is offline.')
				
		except Exception, es:
		
			# If something went wrong, record a DownTime object:
			DownTime().put();
			self.response.out.write(es)

class OncePerDayHandler(webapp.RequestHandler):

	# The get method is executed once per day,
	# and it creates a new Day entry from the last
	# 24 hours worth of pings.

	def get(self):
	
		query = db.GqlQuery("SELECT * FROM Ping WHERE date>:dt", dt=(datetime.now() - timedelta(hours = 24)))
		
		allPings = query.fetch(limit=300)
		
		totResponseTime = 0
		avgResponseTime = 0;
		
		for ping in allPings:
			totResponseTime+= ping.responseTime

		if len(allPings)>0:
			avgResponseTime = totResponseTime/len(allPings);
		
		query = Day.gql("WHERE date=:dt",dt=datetime.now().date())
		
		if len(query.fetch(limit=1)) == 0:
			Day(averageResponseTime=avgResponseTime,totalPings = len(allPings)).put()
			self.response.out.write("Done!")
		else:
			self.response.out.write("This day already exists in the datastore!");