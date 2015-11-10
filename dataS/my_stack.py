#!/usr/bin/python

import pythonds.basic.stack.Stack
#from pythonds.basic.stack import Stack

class Stack:
    def __init__(self):
        self.items = []
    def sIsEmpty(self):
        return self.items == []
    def sPush(self, item):
        return self.items.append(item)
    def sPop(self):
        return self.items.pop()
    def sPeek(self):
        return self.items[len(self.items) - 1]
    def sSize(self):
        return len(self.items)

s1 = Stack()

p1 = s1.sIsEmpty()
print p1

s1.sPush(3)
s1.sPush(4)
s1.sPush(-1)
s1.sPush(0)
s1.sPush(4)
s1.sPush(1)
s1.sPush(5)

print s1.items

s1.sPop()

print s1.items

print(s1.sPeek())
print(s1.sSize())
