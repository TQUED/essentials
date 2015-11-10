#!/usr/bin/python

import sys

class Rectangle():
    def __init__(self, l, b):
        self.length = l
        self.breadth = b
    def area(self):
        return self.length * self.breadth
    def __cmp(self, other):
        return cmp(self.area, other.area)
    #def __str__(self):
    #    return 'Rectangle of  %s width and %s breadth' %(self.length, self.breadth)
    def __repr__(self):
        return 'Rectangle of  %s width and %s breadth' %(self.length, self.breadth)

objs = [ Rectangle(1, 2), Rectangle(3,4) ]
for obj in objs:
    print(obj)

print sys.argv[0]
#print r.area()
#print r.cmp()
