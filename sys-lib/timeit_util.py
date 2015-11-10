#!/usr/bin/python

from timeit import Timer

c = Timer('b = a * 5', 'a = 2').timeit()
print c
