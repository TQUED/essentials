# url for website        
base_url = 'http://www.myfitnesspal.com'       
# login action we want to post data to       
login_action = '/account/login'       
# file for storing cookies       
cookie_file = 'mfp.cookies'

import urllib, urllib2
import cookielib
 
# set up a cookie jar to store cookies
cj = cookielib.MozillaCookieJar(cookie_file)
 
# set up opener to handle cookies, redirects etc
self.opener = urllib2.build_opener(
     urllib2.HTTPRedirectHandler(),
     urllib2.HTTPHandler(debuglevel=0),
     urllib2.HTTPSHandler(debuglevel=0),            
     urllib2.HTTPCookieProcessor(cj)
)
# pretend we're a web browser and not a python script
opener.addheaders = [('User-agent',
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) '
     'AppleWebKit/535.1 (KHTML, like Gecko) '
     'Chrome/13.0.782.13 Safari/535.1'))
]

# open the front page of the website to set
# and save initial cookies
response = opener.open(base_url)
cj.save()</pre>
Then finally we can call the login action with our username and password and login to the website:
<pre># parameters for login action
login_data = urllib.urlencode({
    'username' : 'my_username',
    'password' : 'my_password',
    'remember_me' : True
})
# construct the url
login_url = base_url + login_action
# then open it
response = opener.open(login_url, login_data)
# save the cookies and return the response       
cj.save()
