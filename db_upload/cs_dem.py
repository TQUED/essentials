#!/usr/bin/python

import csv

r = csv.reader(open("data"))
line1 = r.next()
rel = line1[1]
compn = line1[3]
categ = line1[5]
print rel
print compn
print categ
