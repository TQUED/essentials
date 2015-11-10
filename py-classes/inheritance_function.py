#!/usr/bin/python


class BaseClass(object):
    a = 1
    def __init__(self, name):
        self.name = name


class InheritClass(BaseClass):
    b1 = BaseClass('suraj')
    def __init__(self, name1):
        self.name1 = name1


obj = InheritClass('niraj')
print obj.a
print obj.name1
print obj.b1.name
