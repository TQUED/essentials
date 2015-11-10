#!/usr/bin/python

class Queue:

    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enQueue(self, item):
        self.items.insert(0, item)
    def deQueue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

q1 = Queue()
r1 = q1.isEmpty()

q1.enQueue(-1)
q1.enQueue(0)
q1.enQueue(100)
q1.enQueue(11)
q1.enQueue(10)
q1.enQueue(-100)
q1.enQueue('Kiwi')
q1.enQueue('Kangaroo')

r2 = q1.isEmpty()
r3 = q1.deQueue()
