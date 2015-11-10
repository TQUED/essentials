#!/usr/bin/env python
'''
This is a python based utility to comapre current
test runs with baseline test run and provide output  
'''
import argparse, sys

TRUN_PATH="/home/netstorm/work/logs/"
USAGE = "\nINFO : Python Testrun compare utilities\nUSAGES:"

def print_usages():
    print USAGE

def compare_trun(baseline, current):
        

def main():
    btrun = sys.argv[1]
    ctrun = [] 
    argflag = False    

    for arg in sys.argv[2:]:
        ctrun.append(arg)
   
    if len(sys.argv) == 0 or len(sys.argv) == 1:
        print_usages()
    else:
        argflag = True

    if argflag:
        compare_trun(btrun, ctrun)


if __name__ == '__main__':
    main()
