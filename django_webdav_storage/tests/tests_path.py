# coding: utf-8
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
import os

from django_webdav_storage.tests import TestBase, LAZY_FOX


class TestPathMethod(TestBase):
    """
    Tests for `path` storage method
    """
    def test_path_non_exists(self):
        self.assertIsNone(
            self.storage.path(self.session_id + '_non_exists.txt')
        )

    def test_path_exists(self):
        with self.existing_file('exists.txt') as f:
            path = self.storage.path(f.filename)
            self.assertTrue(os.path.exists(path))
            self.storage.delete(f.filename)
            self.assertIsNone(self.storage.path(f.filename))

    def test_path_file_content(self):
        with self.existing_file('exists.txt') as f:
            path = self.storage.path(f.filename)
            with open(path) as tmp:
                self.assertEqual(tmp.read(), LAZY_FOX)
