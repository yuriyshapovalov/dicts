#!/usr/bin/env python

''' Database initializer

This module implement database initializer which provide functionality to
parse dict files, and update or create daabase content.
'''
import sys
from pymongo import MongoClient

class Dict(object):

    def __init__(self):
        self.words = []

    def addWord(self, id, word):
        if word:
            self.words.append(Word(id, word))

    def setMeta(self, language, category)
        if language:
            self.language = language

        if category:
            self.category = category


class Word(object):

    def __init__(self, id, word):
        self.id = id
        self.word = word

class DictionaryParser(object):

    def __init__(self):
        pass

    def parse(self, dict_path):
        if not dict_path:
            raise Exception("Error: Path to dictionaty file is not provided")

        self.dict = Dict()
        with open(dict_path, 'r') as file:
            self.parseTitle(file.readline())
            for line in file:
                self.parseWord(line)

        return self.dict

        def parseTitle(self, string):
            if not string:
                raise Exception("Error: Title string is empty")
            if string[0] not '>':
                raise Exception("Error: Dictionary file format incorrect")
            arr = string[1:].split('|')
            language = arr[0].strip()
            category = arr[1].strip()
            self.dict.setMeta(language, category)

        def parseWord(self, string):
            if not string:
                raise Exception("Error: Word string is empty")
            arr = string.split('|')



def main():
    connection = MongoClient("connectionstring");
    parser = DictionaryParser()
    parser.parse()


if __name__ == '__main__':
    main()