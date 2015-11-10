#!/usr/bin/python

import textwrap

doc = """Trident Academy of technology is a renowned and premere
technology based educational institution in India, where a bunch
of entrepreneural minds appear. Thats make trident as the silicon
valley of odisha."""

print textwrap.fill(doc, width=40)
print(len(doc))
