#!/usr/bin/python

import subprocess

a = print((subprocess.check_output("cat data | cut -d ',' -f2 | awk 'NR==1'", shell=True)).strip())
print a
