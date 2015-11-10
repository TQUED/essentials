#!/usr/bin/python

class Dog(object):
    def __init__(self, name):
        self.name = name
        self.trick = []
    
    def add_trick(self, trick):
        self.trick.append(trick)

d1 = Dog('Pomeranian')
d2 = Dog('Shepeherd')

d1.add_trick('Bunch Hair')
d2.add_trick('Long Body')

print d1.name
print d2.name

print d1.trick
print d2.trick
