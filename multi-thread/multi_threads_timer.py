#!/usr/bin/python

import logging
import time
import threading

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-s) %(message)s',)

def n():
    logging.debug('Inside n thread....')

def n1():
    logging.debug('Inside n1 thread....')
    time.sleep(5.0)
    logging.debug('sleep done')

#Avoiding imported module print functions
if __name__ == '__main__':
    #Instatiating thread timer object
    th1 = threading.Timer(5.0, n)
    th2 = threading.Timer(5.0, n1)
    
    #Initializing thread names
    th1.setName('t1')
    th2.setName('t2')

    #Starting thread instances
    logging.debug('starting timers......')
    th1.start()
    th2.start()
   
    #Look for timer functionalities 
    logging.debug('waiting before cancelling %s', th1.getName())
    time.sleep(2)
    logging.debug('cancelling %s', th1.getName())
    print 'before cancelling th1.isAlive() =', th1.isAlive()
    th1.cancel()
    time.sleep(1)
    print 'after cancelling th1.isAlive() =', th1.isAlive()

    th1.join()  
    th2.join()  
  
    logging.debug('threading done')
