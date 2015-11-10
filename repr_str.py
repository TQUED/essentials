#!/usr/bin/python

#  convert any value to a string: pass it to the repr() or str()

s = 'Hello, world.'
print str(s)

print repr(s)

print str(0.1)

print repr(0.1)

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print s

# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print hellos   # 'hello, world\n'

# The argument to repr() may be any Python object:
print repr((x, y, ('spam', 'eggs')))

# reverse quotes are convenient in interactive sessions:
print `x, y, ('spam', 'eggs')`
