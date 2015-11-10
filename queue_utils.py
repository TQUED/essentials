#!/usr/bin/python

from collections import queue.Queue

queue = deque(["Bentley", "Ford", "Alfa Romeo", "Ducati", "Tesla", "Chevron", "Volta", "Tata", "Augusta"])

print queue

queue.append("Tatra")
queue.append("Mercedes")

print queue

queue.popleft()

print queue
