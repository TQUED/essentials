#!/usr/bin/python

class MyClass():
    def __init__(self):
        self.__superprivate = "Hello"
        self._semiprivate = ", World!"
mc = MyClass()

print mc._MyClass__superprivate
#print mc._semiprivate
#print mc.__dict__
