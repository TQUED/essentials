#Python code to get numerator and denominator of a fraction

#!/usr/bin/python

import fractions

def get_numerator(num):
    return num.numerator
def get_denominator(num):
    return num.denominator

f = fractions.Fraction(1, 2)
print 'Fraction is : ', f

n = get_numerator(f)
d = get_denominator(f)

print 'Numerator is {0} and denominator is {1}'.format(n, d)
