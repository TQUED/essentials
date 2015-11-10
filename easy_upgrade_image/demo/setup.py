from distutils.core import setup

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
files = ["things/*"]

setup(name = "appname",
    version = "0.0.1",
    description = "pyEasyUpgrade",
    author = "nirajKpanda",
    author_email = "nirajpanda@outlook.com",
    url = "https://github.com/nirajKpanda",
    packages = ['upgrad'],
    package_data = {'package' : files },
    scripts = ["runner"],
    long_description = """Really long text here.""" 
) 

classifiers=[
      'Development Status :: 4 - Beta',
      'Environment :: X11 Applications :: GTK',
      'Intended Audience :: End Users/Desktop',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GNU General Public License (GPL)',
      'Operating System :: POSIX :: Linux',
      'Programming Language :: Python',
      'Topic :: Ubuntu or Linux command line',
      'Topic :: webservices to effective build management']
