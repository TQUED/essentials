#!/usr/bin/python

import urllib2

for line in urllib2.urlopen('http://www.google.com'):
	if 'EST' in line:      # look for Eastern Standard Time
	    print line
        else:
            print "not found"

#import smtplib

#server = smtplib.SMTP('localhost')
#server.sendmail('soothsayer@tmp.org', 'jceasar@tmp.org',
#"""To: jceasar@tmp.org
#From: soothsayer@tmp.org

#Beware the Ides of March.
#""")
#server.quit()
