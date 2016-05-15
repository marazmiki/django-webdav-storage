# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from django import test
from django_webdav_storage.tests import TestBase, EMPTY_GIF, LAZY_FOX
from django.utils import six


class TestOpenMethod(TestBase):
    """
    Tests for `_open` storage method
    """
    def test_get_binary_file(self):
        with self.existing_file('empty.gif', content=EMPTY_GIF) as f:
            content = self.storage._open(f.filename, 'rb')
            self.assertEquals(EMPTY_GIF, content.read())

    @test.utils.skipIp(six.PY3, 'Does not work in Python 3.x')
    def test_get_text_mode(self):
        with self.existing_file('file.txt', content=LAZY_FOX) as f:
            content = self.storage._open(f.filename, 'r')
            self.assertEquals(LAZY_FOX, content.read())
