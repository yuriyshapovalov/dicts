#!/usr/bin/env python

''' Web Crawler/Spider

This module implements web crawler. Functionality allows 
to search words in the web, and updates rank system in database.
Words which is not recognized by the system 
(does not present in dictionaries) will be added to "unknown words"
for particular language
'''

__version__ = '0.1'
__author__ = 'Yuriy Shapovalov'
__author_email__ = 'shapovalov.yuri@gmail.com'


import sys
import time
import math
import urllib2
import urlparse

class Crawler(object):

    def __init__(self, root, depth):
        self.root = root
        self.depth = depth
        self.host = urlparse.urlparse(root)[1]
        self.urls = []

    def crawl(self):
        pass

def main():
    pass


if __name__ == '__main__':
    main()