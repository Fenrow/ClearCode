"""
Python Intern Task - Web Crawler

Write a function `site_map(url)` that takes a site URL as an argument and
creates a mapping of that domain as a Python dictionary.
The mapping should contain all the accessible pages within that domain.
Every entry should consist of:
* key: URL
* value: dictionary with:
** site title (HTML `<title>` tag)
** links - set of all target URLs within the domain on
the page but without anchor links
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

map = {}
domain_url = 'http://localhost:8000'

def site_map(url):
    """Function return a dictionary with URL:{site_title: Title,
    links: set of all target URLs}"""

    #Variables
    global domain_url
    len_domain_name = len(domain_url)

    #creating 'soup'
    data = urlopen(url).read()
    soup = BeautifulSoup(data, 'html.parser')
    links =[]

    #Searching for all links
    for link in soup.findAll('a'):
        #link end with '.html' or is a main site
        if link['href'][-5:] == '.html' or link['href'] == domain_url:
            links.append(link.get('href'))

    links_dict = set(links)
    map[url] = {}
    map[url]['title'] = soup.title.string
    map[url]['links'] = links_dict

    #jump to another site from links[]
    for link in links:
        #if link have 'domain_url' only add rest of the link
        if domain_url in link:
            if link == domain_url:
                new_link = domain_url
            else:
                new_link = domain_url + link[len_domain_name:]

            if new_link in map:
                break
            else:
                site_map(new_link)
        #if heve'nt 'domain_url' add entire link to domain_url
        elif '.html' in link:
            new_link = domain_url + link

            if new_link in map:
                break
            else:
                site_map(new_link)

    return map

print(site_map(domain_url))
