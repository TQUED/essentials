#!/usr/bin/python

def add(x,y): return x+y

r=reduce(add, range(1, 3))
print r 

def cube(x): return x*x*x

s=map(cube, range(1,5))
print s
