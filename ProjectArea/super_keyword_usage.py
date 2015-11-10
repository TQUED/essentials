#!/usr/bin/env python

'''
super() lets you avoid referring to the base class explicitly, 
which can be nice. But the main advantage comes with multiple 
inheritance, where all sorts of fun stuff can happen.

With super keyword we can achieve an extra layer of indirection
in __init__ module, which refferences the base class

This means that the use of super can make your code more maintainable 
when you have child classes referencing methods of their parents 
directly, most likely because they have overridden those methods themselves.

Another mostly hidden difference is that super is returning a proxy object 
to handle the delegated call to __init__, and is passing self as an implied 
first argument to the __init__ call (you may have wondered why it appears 
to be missing).

In multiple inheritance case if a resource wants to access the child class
resources. super keyword enables for this need. And make available of the
right resource need to be used by the class instance.

Needful web links:
1. http://learnpythonthehardway.org/book/ex44.html
2. https://rhettinger.wordpress.com/2011/05/26/super-considered-super/
'''

class Polygon(object):
    def __init__(self, id):
        self.id = id


class Rectangle(Polygon):
    def __init__(self, id, width, height):
        super(self.__class__, self).__init__(id)
        self.shape = (width, height)


class Square(Rectangle):
    pass


class Parent1(object):
    def __init__(self, id):
        self.id = id


class Parent2(object):
    def __init__(self, id):
        self.id = id


class Child(Parent1, Parent2):
    def __init__(self, id):
        self.id = id
        super(Child, self).__init__()


c = Child('a')
print c.id
