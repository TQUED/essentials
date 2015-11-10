#!/usr/bin/python

def average(values):
    try:
        return sum(range(values), 0.0)/len(range(values))
    except(Exception):
        raise "vailueError arrises"

average(range(10))
import doctest
doctest.testmod()
