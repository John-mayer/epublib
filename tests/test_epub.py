# -*- coding: utf-8 -*-
import unittest

from epublib import epub

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = epub.Book()

    def test_mimetype(self):
        # the content of mimetype in epub3 file is unchangeable.
        self.assertEqual(self.book.mimetype, 'application/epub+zip')

