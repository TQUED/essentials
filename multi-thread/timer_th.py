#!/usr/bin/python

import threading

def sayHello():
    print("Hello Sunil : Happy Birthday")

t = threading.Timer(0.9, sayHello)
t.start()
