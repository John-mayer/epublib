# -*- coding: utf-8 -*-

class Book(object):
    def __init__(self, title=''):
        self.__title = title

    @property
    def title(self):
        """Get the book title"""
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title
