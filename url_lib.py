#!/usr/bin/python

import urllib2

req = urllib2.Request('http://www.youtube.com')
try:
    rep = urllib2.urlopen(req)
except HTTPError as e:
    print e.code
    print e.read()
