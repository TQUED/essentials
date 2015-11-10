#!/usr/bin/python

import random

a =random.choice(['niraj', 'panda', 'kumar'])
print a

b = random.choice(range(10))
print b

#c = xrange(10)
#print c

d = random.sample(xrange(100), 15)
print d

e = random.random()
print e

f = random.randrange(10)
print f
