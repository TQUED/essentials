#!/usr/bin/python

for x in range(1,10):
    print '{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)
#    print(repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4))
