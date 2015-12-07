# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os


class Book(object):
    def __init__(self, title='', lang='en', author='', publisher='',
                 copyright_desc='', package_doc_name='content.opf',
                 nav_doc_name='toc.xhtml'):
        self.__mimetype = 'application/epub+zip'
        self.title = title
        self.lang = lang
        self.author = author
        self.publisher = publisher
        self.copyright = copyright_desc
        self.package_doc_name = package_doc_name
        self.nav_doc_name = nav_doc_name

    @property
    def mimetype(self):
        """Get the mimetype"""
        return self.__mimetype

    @mimetype.setter
    def mimetype(self, mimetype):
        """The content of mimetype is unchangeable."""
        pass


class Writer(object):
    def make_mimetype(self, book, filepath):
        """Write down mimetype file to the path."""
        filename = 'mimetype'

        with open(os.path.join(filepath, filename), 'w') as f:
            f.write(book.mimetype)
