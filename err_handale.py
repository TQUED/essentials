#!/usr/bin/python

import math

def ops(val):
    if val < 0:
        raise "Value can never be in negative"
    else:
        print(math.sqrt(val))
ops(-2.3)
