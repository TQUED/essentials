#!/usr/bin/python

from heapq import heapify, heappop, heappush 

marks = [1, 0, -1, 3, -7, 99, 21, 34, 0.1]
print marks

heapify(marks)
print marks

heappush(marks, 100)
print marks

a = [heappop(marks) for i in range(3)]
print a
print marks
