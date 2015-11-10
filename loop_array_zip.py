#!/usr/bin/python

states = ['odisha', 'bihar', 'chatishgarh']
cities = ['bbsr', 'patna', 'vilai']

for s, c in zip(states, cities):
    print 'state {0} has {1} city inside it'.format(s, c)
