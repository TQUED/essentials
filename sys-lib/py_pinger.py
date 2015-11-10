#!/usr/bin/python

from threading import Thread
import subprocess
from Queue import Queue

#Global variables declaration
num_threads = 4
queue = Queue()
ips = ["www.google.com", "www.yahoo.com", "www.facebook.com", "10.10.30.37"]

#wraps system ping command
def pinger(i, q):
    """Pings subnet"""
    while True:
        ip = q.get()
        print "Thread %s: Pinging %s" % (i, ip)
        ret = subprocess.call("ping -c 1 %s" % ip,
            shell=True,
            stdout=open('/dev/null', 'w'),
            stderr=subprocess.STDOUT)
        if ret == 0:
            print "%s: is alive" % ip
        else:
            print "%s: did not respond" % ip
        q.task_done()

#Spawn thread pool
for i in range(num_threads):

    worker = Thread(target=pinger, args=(i, queue))
    worker.setDaemon(True)
    worker.start()
    print "Main program contnues executing in background"
    
#Place work in queue
for ip in ips:
    queue.put(ip)

#Wait until worker threads are done to exit    
queue.join()
print "Threads wait untill the main program stops execution"
