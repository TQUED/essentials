#!/usr/bin/env python

import Queue
import threading
import urllib2


def get_url(q, u):
    q.put(urlilib2.urlopen(u).read())

urls = ["http://10.10.30.37:5000", "https://github.com"]
q = Queue.Queue()

for u in urls:
    t = threading.Thread(target=get_url, args = (q, u))
    t.daemon = True
    t.start()

s = q.get()
print s
