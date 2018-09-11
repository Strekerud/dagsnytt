#!/usr/bin/env python
# coding:utf-8

import requests
from xml.etree import ElementTree
from fabric.colors import blue, green, red, yellow

def getBBCWorldNews():
    api_url = "http://feeds.bbci.co.uk/news/world/rss.xml"

    print green("=== BBC World News Feed ===")
    
    response = requests.get(api_url)

    tree = ElementTree.fromstring(response.content)

    content = [(item.find('title').text.encode('utf-8'), item.find('description').text.encode('utf-8'), (item.find('link').text.encode('utf-8'))) for item in tree.findall('./channel/item')]

    for title, description, link in content[:5]:
        print '- {} -'.format(yellow(title))
        print description
        print "Link: " + red(link)
