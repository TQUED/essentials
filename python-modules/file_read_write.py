#!/usr/bin/python

o = open('hadoop', 'w')

value = "INDIA india INDIA india"
s = str(value)

o.write(s)
p = o.tell()
print p
o.seek(0, 1)
p1 = o.tell()
print p1
