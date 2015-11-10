#!/usr/bin/python

def f(x): return x % 2 != 0 and x % 3 != 0

#n = int(raw_input("Enter numner to filter the sequence: "))
res=filter(f, range(2, 25))

print res
