#!/usr/bin/env python
import sys

def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line


def grep(pattern, lines):
    return (line for line in lines if pattern in lines)


def printlines(lines):
    for line in lines:
        print line,


def main(pattern, filenames):
    lines = readfiles(filenames)
    lines = grep(pattern, lines)
    printlines(lines)


pattern = sys.argv[1]
filenames = sys.argv[2]

main(pattern, filenames)
