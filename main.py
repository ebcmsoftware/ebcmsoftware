import webapp2
import os
from google.appengine.ext.webapp import template
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Donate(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('donate.html')
        self.response.write(template.render({}))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render({}))

app = webapp2.WSGIApplication([
    ('/donate', Donate),
    ('/', MainHandler)
], debug=True)
