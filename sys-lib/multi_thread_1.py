#!/usr/bin/python

import threading
import socket

class MultThrd(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        try:
            ping.verbose_ping('www.google.com', count=3)
        except Socket.error, e:
            print "Ping error : ", e


        
background = MultThrd()

background.start()
print 'The main program continues to run in foreground.'

background.join()    # Wait for the background task to finish
print 'Main program waited until background was done.'
