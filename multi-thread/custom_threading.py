#!/usr/bin/python

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

class MyThread(threading.Thread):

    def __init__(self, args=(), kwargs=None, name=None):
	super(MyThread,self).__init__()
	self.args = args
	self.kwargs = kwargs
	return

    def run(self):
	logging.debug('Effective thread is %s and %s', self.args, self.kwargs)
	return

if __name__ == '__main__':
    for i in range(3):
	t = MyThread(args=(i,), kwargs={'a':i, 'b':i+=1})
	t.start()
