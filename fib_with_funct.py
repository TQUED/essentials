#!/usr/bin/python


#Function Definition Part
def fib(n):

 a, b = 0, 1
 while b < n:
   print b,
   a, b = b, a+b


#Function Call part
x = int(raw_input("Please Enter a number : "))
if x < 0:
    print 'You have entered a negative integer value!!!!Oooops'
else:
    fib(x)
