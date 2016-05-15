# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from django.utils import six
from django_selectel_storage.tests import TestBase, EMPTY_GIF, LAZY_FOX


class TestSizeMethod(TestBase):
    """
    Tests for `url` storage method
    """
    def test_size_for_non_existing_file(self):
        with self.assertRaises(IOError):
            self.storage.size(self.session_id + '_non_exists.txt')

    def test_zero_size_file(self):
        with self.existing_file('zero_size.txt') as f:
            self.assertEquals(0, self.storage.size(f.filename))

    def test_size_binary_file(self):
        with self.existing_file('empty.gif', content=EMPTY_GIF) as f:
            self.assertEquals(len(EMPTY_GIF), self.storage.size(f.filename))

    def test_size_text_file(self):
        if six.PY3:
            self.skipTest('Does not work in py3')

        with self.existing_file('README.md', content=LAZY_FOX) as f:
            self.assertEquals(len(LAZY_FOX), self.storage.size(f.filename))
