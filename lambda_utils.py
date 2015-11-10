#!/usr/bin/python

def add(n):
    return lambda x: x + n
a = add(0)

a(0)

print a

a(42)

print a
