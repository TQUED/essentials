#!/usr/bin/python

def sum(seq):
    def add(x,y):
        return x+y
    return reduce(add, seq, 0)

a = sum(range(1,10))

print a
