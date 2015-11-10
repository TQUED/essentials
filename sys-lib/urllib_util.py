#!/usr/bin/python

import urllib2

for u in urllib2.urlopen('http://www.cavisson.com'):
    if 'X' in u or 'W' in u:
        print u
