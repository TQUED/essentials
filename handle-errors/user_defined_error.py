#!/usr/bin/python

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return float(repr(self.value))

try:
    raise MyError(9/2)
except MyError as e:
    print('My Exception occured, value:', e.value)
