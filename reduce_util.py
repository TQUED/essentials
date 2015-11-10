#!/usr/bin/python

def add(x,y):
    return x+y

a = reduce(add, range(10))

print a
