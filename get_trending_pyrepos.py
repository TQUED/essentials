#!/usr/bin/env python

import urllib2
from BeautifulSoup import BeautifulSoup

URL = "https://github.com/trending/python"


def get_name_value_dict(repos_html):
    hash_list = []
    
    for repo_li in repos_html:
        author_or_org, repo_name = str(repo_li.findAll('a')[1].text).split('/')
        desc = repo_li.find('p').text
        entry = { 'author/org' : author_or_org, 'repo' : repo_name, 'description' : desc }
        hash_list.append(entry)

    return hash_list


def main():
    data = urllib2.urlopen(URL).read()
    data = BeautifulSoup(data)
    repos =  data.findAll('li', attrs={'class': 'repo-list-item'})

    # get repo wise name-value pair
    name_value_dict = get_name_value_dict(repos)
    
    for num, item in enumerate(name_value_dict):
        print '{} ---> {}'.format(num, item)

if __name__ == '__main__':
    main()
