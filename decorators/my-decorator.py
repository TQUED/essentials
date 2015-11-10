#!/usr/bin/python

def show(in_func):    
    def out_function(in_func):
        return "Sum is" str(in_func)
    return out_func

@show
def entries(n1, n2):
    return n1 + n2

print entries(23, 31)
