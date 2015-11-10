#!/usr/bin/python

import time, os.path
from string import Template

docfiles = ['m2_v1.pdf', 'v1_m3.ppt', 'm3_vol2.jpeg']

class BatchRename(Template):
    delimeter = '|'

f = raw_input('Enter rename style (%d-date %n-seqnum %f-format): ')
t = BatchRename(f)

d = time.strftime('%d|%b|y')
for i, filename in enumerate(docfiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print '{0} --> {1}'.format(filename, newname) 
