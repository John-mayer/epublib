# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from .templates import template_container_xml


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
    def make_mimetype(self, book, outputpath):
        """Write down mimetype file to the path."""
        filename = 'mimetype'

        with open(os.path.join(outputpath, filename), 'w') as f:
            f.write(book.mimetype)

    def make_container_xml(self, book, outputpath):
        """Write down container.xml"""
        try:
            os.mkdir(os.path.join(outputpath, 'META-INF'))
        except OSError:
            # META-INF directory exists and then it is needless to do something.
            pass

        with open(os.path.join(outputpath, 'META-INF/container.xml'), 'w') as f:
            f.write(template_container_xml.format(
                os.path.join('OEBPS', book.package_doc_name)))

