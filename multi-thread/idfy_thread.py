#!/usr/bin/python

import threading
import time

def t1():
    print threading.currentThread().getName(), 'starting'
    time.sleep(1)
    print threading.currentThread().getName(), 'exiting'
def t2():
    print threading.currentThread().getName(), 'starting'
    time.sleep(2)
    print threading.currentThread().getName(), 'exiting'
def t3():
    print threading.currentThread().getName(), 'starting'
    time.sleep(3)
    print threading.currentThread().getName(), 'exiting'

th1 = threading.Thread(target=t1)
th2 = threading.Thread(target=t2)
th3 = threading.Thread(target=t3)

th1.start()
th2.start()
th3.start()
