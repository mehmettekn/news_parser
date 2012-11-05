#!/usr/bin/env python

import random
from models.models import *
from datetime import datetime,timedelta
from google.appengine.ext import webapp, db

# This class will help you generate test data.
# If you need to, you can execute it by 
# Navigating to /generate-test-data/

class GenerateTestData(webapp.RequestHandler):
	def get(self):
	
		for p in Ping.all().fetch(limit=500):
			p.delete()
			pass
		for d in Day.all().fetch(limit=100):
			d.delete()
			pass
	
		for i in range(288):
			Ping(date=(datetime.now()-timedelta(minutes=i*5)),responseTime=random.randint(700,2000)).put()
		for i in range(30):
			Day(date=(datetime.now()-timedelta(days=i)).date(),averageResponseTime=random.randint(700,2000)).put()
			pass
		self.response.out.write("Your test data was created!");