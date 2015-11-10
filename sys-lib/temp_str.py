#!/usr/bin/python

from string import Template

a = Template('${state} has the ${typ} name as ${name}.')
a.substitute(state='odisha', typ='capital', name='bhubaneswar')

print a
