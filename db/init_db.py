#!/usr/bin/env python
import sys
from pymongo import MongoClient

class Dict(object):
    def __init__(self, language, category='undefined'):
        self.language = language
        self.category = category
        self.words = []

class Word(object):
    def __init__(self):
        pass

class DictionaryParser(object):
    def __init__(self):
        pass

def main():
    connection = MongoClient("connectionstring");


if __name__ == '__main__':
    main()