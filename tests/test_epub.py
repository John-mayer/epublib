# -*- coding: utf-8 -*-
import os
import unittest
import tempfile
import shutil

from epublib import epub
from epublib.templates import template_container_xml


class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = epub.Book()

    def test_mimetype(self):
        # the content of mimetype in epub3 file is unchangeable.
        self.assertEqual(self.book.mimetype, 'application/epub+zip')


class TestWriter(unittest.TestCase):

    def setUp(self):
        self.writer = epub.Writer()
        self.tempdir = tempfile.mkdtemp(dir=os.getcwd())

    def tearDown(self):
        shutil.rmtree(self.tempdir)

    def test_make_mimetype(self):
        filepath = os.path.join(self.tempdir, 'mimetype')
        self.writer.make_mimetype(epub.Book(), self.tempdir)

        with open(filepath, 'r') as mimetype:
            self.assertEqual(mimetype.read(), 'application/epub+zip')

    def test_make_container_xml(self):
        container_xml_path = os.path.join(self.tempdir,
                                          'META-INF/container.xml')
        self.writer.make_container_xml(
            epub.Book(package_doc_name='content.opf'), self.tempdir)

        with open(container_xml_path, 'r') as container_xml:
            self.assertEqual(container_xml.read(),
                             template_container_xml.format('OEBPS/content.opf'))
