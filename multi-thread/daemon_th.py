#!/usr/bin/python

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(levelname)s] (%(threadName)-s) %(message)s',)

def t1():
    logging.debug('starting')
    #time.sleep(10)
    logging.debug('exiting')
def t2():
    logging.debug('starting')
    for i in range(5):
        print("Hi Daemon")
        time.sleep(1) 
    logging.debug('exiting')
if __name__ == '__main__':
    th1 = threading.Thread(name='non-daemon', target=t1)
    th2 = threading.Thread(name='daemon', target=t2)
    th2.setDaemon(True)
    
    th1.start()
    th2.start()
   
    th2.join(4.1)
    print 'th2.isAlive()', th2.isAlive()
    th1.join(2.5)
