#!/usr/bin/python

import csv
import sys

infile = sys.argv[1]

f = csv.reader(open('%s' %infile))
f.next()
r = f.next()
print r
