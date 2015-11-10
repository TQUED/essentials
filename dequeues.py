#!/usr/bin/python

class DeQueue:

    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def addFront(self, item):
        self.items.append(item)
    def addRear(self, item):
        self.items.insert(0, item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)

d1 = DeQueue()

#print(d1.isEmpty())
#print(d1.size())
d1.addFront(1)
#print(d1.items)
d1.addFront('a')
#print(d1.items)
d1.addRear(2)
#print(d1.items)
d1.addRear('b')
#print(d1.items)
d1.removeFront()
#print(d1.items)
d1.removeRear()
#print(d1.items)
#print(d1.size())
