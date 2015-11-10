#!/usr/bin/python

import threading
import time
import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

def f():
    t = threading.currentThread()
    r = random.randint(1,10)
    logging.debug('Starting %s', r)
    time.sleep(r)
    logging.debug('Ending')
    return

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=f)
        t.setDaemon(True)
	t.start()

    main_thread = threading.current_thread()
    for t in threading.enumerate():
	if t is main_thread:
		continue
	logging.debug('joining %s', t.getName())
	t.join()
