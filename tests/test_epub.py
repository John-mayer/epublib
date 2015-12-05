# -*- coding: utf-8 -*-
import unittest

from epublib import epub

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = epub.Book()

    def test_title(self):
        # default epub book title is empty string.
        self.assertEqual(self.book.title, '')

        self.book.title = 'sample-book'
        self.assertEqual(self.book.title, 'sample-book')
