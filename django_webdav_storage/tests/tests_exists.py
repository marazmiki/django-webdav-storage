# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from django_webdav_storage.tests import TestBase


class TestExistsMethod(TestBase):
    """
    Tests for `exists` storage method
    """
    def test_exists_not(self):
        filename = self.session_id + '_non_exists.txt'
        self.assertFalse(self.storage.exists(filename))

    def test_exists_yes(self):
        with self.existing_file('file.img') as f:
            self.assertTrue(self.storage.exists(f.filename))
