#!/usr/bin/python

from dequeues import DeQueue

def palcheck(str):
    d = DeQueue()

    for c in str:
        d.addRear(c)
    
    flag = True
    while d.size() > 1 and flag:
        a = d.removeFront()
        b = d.removeRear()
        if a != b:
            flag = False
            return flag
    return flag
print(palcheck('1313'))
print(palcheck('12121'))
