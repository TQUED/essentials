#!/usr/bin/python

for x in range(1, 11):
    print repr(x).rjust(1), repr(x*x).rjust(2), repr(x*x*x).rjust(2)
    # Note trailing comma on previous line
    #print repr(x*x*x).rjust(3)

    
#print '================================================='     
#for x in range(1,10):
#    print '%2d %3d %4d %5d' % (x*x, x*x*x, x*x*x*x, x*x*x*x*x)

#for x in range(1, 11)
#   print repr(x),
