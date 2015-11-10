#!/usr/bin/python


def bold(f):
    def wrapped1(*args, **kwargs):
        return '<b>' + f(*args, **kwargs) + '</b>'
        return 'world is saying' + f(*args, **kwargs) 
    return wrapped1


def italic(f):
    def wrapped2(*args, **kwargs):
        return '<i>' + f(*args, **kwargs) + '</i>'
        return ' ' + f(*args, **kwargs) + ' ' +'to automation'
    return wrapped2


@bold
@italic
def hello(name, age):
    return 'hello ' + name


p = hello('niraj', 23)
print p
