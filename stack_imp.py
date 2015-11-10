#!/usr/bin/python

i=1

while 1:

 stack = [2,5,1,0,4]

 print stack

 stack.append(6)
 stack.append(10)

 print stack
 break

x=stack.pop()
print "Popped" ,x
print stack

#stack.push(100)
#print stack
