#!/usr/bin/python

import bisect

scores = [(100, 'perl'), (200, 'ada'), (500, 'smalltalk'), (300, 'oak')]
print scores

bisect.insort(scores, (400, 'ruby'))
print scores
