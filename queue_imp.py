#!/usr/bin/python

queue = ["Eric", "John", "Michael"]
print queue
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print queue

s=queue.pop(0)
print s
print queue

s=queue.pop(0)
print s
print queue

t=queue.push("ramesh")
print queue
