#!/usr/bin/env python

import os
from datetime import datetime
from config import config

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

# This controller handles the
# generation of the front page.

class MainHandler(webapp.RequestHandler):
	def get(self):
	
		# We are using the template module to output the page.
	
		path = os.path.join(os.path.dirname(__file__), '../views' ,'index.html')
		self.response.out.write(
		
			# The render method takes the path to a html template,
			# and a dictionary of key/value pairs that will be
			# embedded in the page.
			
			template.render( path,{
				"title"	: config.scriptTitle,
				"year"	: datetime.now().strftime("%Y"),
				"domain": config.fetchURL.replace('http://','').replace('/','')
		}))
