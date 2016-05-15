# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from django.test.utils import skipIf
from django.utils import six
from django_webdav_storage.tests import TestBase, EMPTY_GIF, LAZY_FOX


class TestOpenMethod(TestBase):
    """
    Tests for `_open` storage method
    """

    @skipIf(six.PY3, 'Does not support in Python 3.x')
    def test_get_zero_length_str(self):
        with self.existing_file('zero.txt', content='') as f:
            content = self.storage._open(f.filename, 'r')
            self.assertEqual(b'', content.read())

    def test_get_zero_length_byte(self):
        with self.existing_file('zero.txt', content=b'') as f:
            content = self.storage._open(f.filename, 'rb')
            self.assertEqual(b'', content.read())

    def test_get_binary_file(self):
        with self.existing_file('empty.gif', content=EMPTY_GIF) as f:
            content = self.storage._open(f.filename, 'rb')
            self.assertEquals(EMPTY_GIF, content.read())

    @skipIf(six.PY3, 'Does not support in Python 3.x')
    def test_get_text_mode(self):
        with self.existing_file('file.txt', content=LAZY_FOX) as f:
            content = self.storage._open(f.filename, 'r')
            self.assertEquals(LAZY_FOX, content.read())
