#!/usr/bin/python

def listSum(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 0:
        return 0
    else:
        return arr[0] + listSum(arr[1:])
print(listSum([-1,3,-2,6,0,71,90]))
print(listSum([-1]))
print(listSum([]))
