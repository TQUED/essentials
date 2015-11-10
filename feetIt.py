#!/usr/bin/python

import urllib

def fetch_thing(url, params, method):
    params = urllib.urlencode(params)
    if method=='POST':
        f = urllib.urlopen(url, params)
    else:
        f = urllib.urlopen(url+'?'+params)
    return (f.read(), f.code)


content, response_code = fetch_thing(
                              'http://google.com/', 
                              {'spam': 1, 'eggs': 2, 'bacon': 0}, 
                              'POST'
                         )
print content
print response_code
