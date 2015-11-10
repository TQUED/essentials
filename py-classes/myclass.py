#!/usr/bin/python


class PrintComplex:
    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary

cn = PrintComplex(-2, -3)
print "Complex object formed is : " + "%s + %si" %(cn.r, cn.i)
