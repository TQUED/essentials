#! /usr/bin/python
import urllib, urllib2
import cookielib
import sys

class WebLogin(object):

    def __init__(self, username, password):
        
        self.base_url = '10.10.30.37:5000'
        self.login_action = '/account/login'
        self.cookie_file = 'login.cookies'

        self.username = username
        self.password = password

        self.cj = cookielib.MozillaCookieJar(self.cookie_file)

        self.opener = urllib2.build_opener(
            urllib2.HTTPRedirectHandler(),
            urllib2.HTTPHandler(debuglevel=0),
            urllib2.HTTPSHandler(debuglevel=0),
            urllib2.HTTPCookieProcessor(self.cj)
        )

        self.opener.addheaders = [('User-agent', 
            ('Mozilla/4.0 (compatible; MSIE 6.0; '
            'Windows NT 5.2; .NET CLR 1.1.4322)'))
        ]

        response = self.opener.open(self.base_url)
        self.cj.save()

        response = self.login()

        print response.read()
        
    def login(self):

        login_data = urllib.urlencode({
            'username' : self.username,
            'password' : self.password,
            'remember_me' : True
        })

        login_url = self.base_url + self.login_action
        response = self.opener.open(login_url, login_data)
        self.cj.save()
        return response


if __name__ == "__main__":

    args = sys.argv

    if len(args) != 3:
        print "Incorrect number of arguments"
        print "Argument pattern: username password"
        exit(1)

    username = args[1]
    password = args[2]

    WebLogin(username, password)


