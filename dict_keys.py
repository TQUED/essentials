#!/usr/bin/python

name = dict([('a', 1), ('b', 2), ('c', 3)])

name['e'] = 5

print name
print name.keys()
x = 'd' in name
print x
