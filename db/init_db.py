#!/usr/bin/env python

''' Database initializer

This module implement database initializer which provide functionality to
parse dict files, and update or create database content.
'''
import sys
from pymongo import MongoClient

class Dict(object):

    def __init__(self):
        self.words = []

    def addWord(self, id, word):
        if word:
            self.words.append(Word(id, word))

    def setMeta(self, language, category):
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

        def parseLine(string):
            if not string:
                raise Exception("Error: Line is empty")

            if string[0] == '#':
                return                        # skip comment string
            elif string[0] == '>':
                try:
                    arr = string[1:].split('|')
                    language = arr[0].strip()
                    category = arr[1].strip()
                    self.dict.setMeta(language, category)
                    #print("language: {} \tcategory: {}".format(self.dict.language, self.dict.category))
                except:
                    raise Exception("Error: Dictionary title has incorrect format")
            else:
                try:
                    arr = string.split('|')
                    word_id = str(arr[0]).strip().translate(None, "[]'") 
                    word = str(arr[1]).strip().translate(None, "'")
                    self.dict.addWord(word_id, word)
                    print("ID: '{}'\tWord: '{}'".format(word_id, word))
                except:
                    raise Exception("Error: Dictionary format is incorrect")

        self.dict = Dict()
        with open(dict_path, 'r') as file:
            for line in file:
                parseLine(line)

        return self.dict

class DatabaseMapper(object):

    def __init__(self, connection_string):
        self.context = MongoClient(connection_string)

    def mapDictionary(self, dict):
        pass

def main():
    DatabaseMapper("mongodb://localhost/dicts");
    parser = DictionaryParser()
    dictonary = parser.parse("../English/verbs.dict")


if __name__ == '__main__':
    main()