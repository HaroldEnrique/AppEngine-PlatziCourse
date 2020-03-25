# -*- coding: utf-8 -*-

import os
import urlib
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        """Return a friendly HTTP greeting"""

        self.response.headers['Content-type'] = 'text/plain'
        self.response.write('Hello world')


app = webapp2.WSGIApplication([
    ('/',MainPage),
], debug = True)