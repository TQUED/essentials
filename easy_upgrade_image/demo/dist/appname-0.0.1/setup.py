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
