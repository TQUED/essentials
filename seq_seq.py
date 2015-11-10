#!/usr/bin/python

seq = range(8)

def add(x,y):
    return x+y

a = map(add, seq, seq)

print a
