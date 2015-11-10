#!/usr/bin/python

class Called:
    def __call__(self, *args, **kwargs):
        print("I have called", args, kwargs)

A = Called()

print A(2015, 'july', 30 , criminal='yakub', crime='terrorirm', punishment='sentenced to death')
