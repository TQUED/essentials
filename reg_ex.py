#!/usr/bin/python

import re

r=re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print r # ['foot', 'fell', 'fastest']

s=re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print s # 'cat in the hat'
