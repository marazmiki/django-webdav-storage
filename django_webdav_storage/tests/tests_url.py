# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from django_webdav_storage.storage import WebDavStorage
from django_webdav_storage.tests import TestBase
import os


class TestUrlMethod(TestBase):
    """
    Tests for `url` storage method
    """
    url = os.getenv('WEBDAV_PUBLIC_URL', 'http://127.0.0.1')

    def _assert(self, url=''):
        with self.settings(WEBDAV_PUBLIC_URL=self.url + url):
            storage = WebDavStorage()
            self.assertEquals(self.url, storage.get_base_url())

    def test_url_with_container_default_name(self):
        self.assertEquals(
            self.storage.get_base_url() + '/index.html',
            self.storage.url('index.html')
        )

    def test_container_custom_name(self):
        self._assert('')

    def test_container_custom_name_trailing_slash(self):
        self._assert('/')

    def test_container_custom_name_trailing_slash_multiple(self):
        self._assert('/////')
