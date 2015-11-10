#!/usr/bin/python

class OutOfRangeError(ValueError): pass
class NotIntegerError(ValueError): pass

def toHexa(n):
    '''convert decimal to hexa'''
    if(n < 0):
        raise OutOfRangeError('number out of range, n < 0 )')

    if not isinstance(n, int):
        raise NotIntegerError('non-integers can not be converted')

    map = ('0','1','2','3','4','5','6','7','8','9',
           'A','B','C','D','E','F')

    s = ''
    while(n/16):
        s += map[n % 16]
        n = n/16

    s += map[n % 16]
    # reverse 
    return s[::-1]
