#!/usr/bin/python

import random

print random.choice(['apple', 'pear', 'banana'])

print random.sample(xrange(100), 10)   # sampling without replacement

print random.random()    # random float

print random.randrange(6)    # random integer chosen from range(6)

print random.random()

print random.randrange(100)
