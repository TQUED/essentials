#!/usr/bin/python

data = {"niraj": 'who', "suraj": 'are', "a": 1, "b": 2, "c": 3, "pooja": "nani"}
print data
print(data.keys())
print(data)
print(data["suraj"])
print(len(data))
print(data.values())
print(sorted(data.keys()))

new = data.copy()

print new
