#!/usr/bin/python

def name(fname: str, age: str = '23') -> str:
    print("Annotations:", name.__annotations__)
    print("Arguments", fname, age)
    return fname + ' and ' + age

name('niraj')
