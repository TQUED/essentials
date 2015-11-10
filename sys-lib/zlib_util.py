#!/usr/bin/python

import zlib

#t = zlib.compress("*.py")

niraj = 'niraj kumar panda is not a person you can believe to'

print(len(niraj))

t1 = zlib.compress(niraj)
print(len(t1))

a = zlib.decompress(t1)
print a

b = zlib.crc32(a)
print b
