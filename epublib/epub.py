# -*- coding: utf-8 -*-
from __future__ import unicode_literals


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
