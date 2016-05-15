# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from django_webdav_storage.tests import TestBase


class TestDeleteMethod(TestBase):
    """
    Tests for `exists` storage method
    """
    def test_delete_non_exists(self):
        self.storage.delete(self.session_id + '_non_exists.txt')

    def test_delete_exists(self):
        with self.existing_file('exists.txt') as f:
            self.assertTrue(self.storage.exists(f.filename))
            self.storage.delete(f.filename)
            self.assertFalse(self.storage.exists(f.filename))
