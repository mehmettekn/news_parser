""" This is the main script. It is imported to all the other scripts as
    a base script. """

import os
import webapp2
import jinja2
import logging

from google.appengine.ext import db

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

def render_str(template, **params):
	t = jinja_environment.get_template(template)
	return t.render(params)	

def render_post(response, post):
	response.out.write('<b>' + post.subject + '</b><br>')
	response.out.write(post.content)	

class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        return render_str(template, **params)

	def set_secure_cookie(self, name, val):
		cookie_val = make_secure_val(val)
		self.response.headers.add_header(
				"Set-Cookie",
				"%s,%s; Path=/" % (name, cookie_val))

	def login(self, user):
		self.set_secure_cookie('user_id', str(user.key().id()))
	

	def logout(self):
		set_secure_cookie(self, 'user_id', None)


	def read_cookie(self, name):
		cookie_val = self.request.get(name)
		if cookie_val and check_secure_val:
				return cookie_val

	def initialize(self, *a, **kw):
		webapp2.RequestHandler.initialize(self, *a, **kw)
		uid = self.read_cookie('user_id')
        self.user = uid and User.by_id(int(uid))
