#!/usr/bin/python

def fib2(n):
 """Return a list containing the Fibonacci series up to n."""
 result = []
 a, b = 0 , 1
 while b < n: 
   result.append(b),
   a, b = b , a+b
 return result

x = int(raw_input("Please Enter a number : "))

if x < 0:
 print 'Negative input check'
else:
 res = fib2(x)
 print res
