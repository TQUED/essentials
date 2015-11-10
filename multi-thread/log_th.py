#!/usr/bin/python

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(levelname)s] (%(threadName)-s) %(message)s')

def t1():
    logging.debug('starting')
    time.sleep(1)
    logging.debug('exiting')
def t2():
    logging.debug('starting')
    time.sleep(2)
    logging.debug('exiting')
def t3():
    logging.debug('starting')
    time.sleep(3)
    logging.debug('exiting')

th1 = threading.Thread(name='log1', target=t1)
th2 = threading.Thread(name='log2', target=t2)
th3 = threading.Thread(name='log3', target=t3)

th1.start()
th2.start()
th3.start()
