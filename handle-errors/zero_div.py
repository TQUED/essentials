#!/usr/bin/python

def this_fails():
    y = 2/2
    print y
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error', err)
