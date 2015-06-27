import webapp2

class Hello(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hi.')

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Bye world :((((((((')

app = webapp2.WSGIApplication([
    ('/hello', Hello),
    ('/', MainHandler)
], debug=True)
