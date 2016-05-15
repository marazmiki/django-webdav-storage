# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from contextlib2 import ExitStack
from django_webdav_storage.tests import TestBase, override_settings
import requests.exceptions


@override_settings(
    WEBDAV_LISTING_BACKEND='django_webdav_storage.listing.nginx_autoindex',
)
class TestListdirMethodNginxAutoindex(TestBase):
    def test_listdir_works(self):
        root = 'test-list/'

        with ExitStack() as stack:
            stack.enter_context(self.existing_file(root + 'file.img'))
            stack.enter_context(self.existing_file(root + 'hello.pdf'))
            stack.enter_context(self.existing_file(root + 'hello/image.png'))
            stack.enter_context(self.existing_file(root + 'hello/text.txt'))

            dirs, files = self.storage.listdir(
                "{0}_{1}".format(self.session_id, root))

            self.assertSetEqual(
                {f for f in files},
                {b'file.img', b'hello.pdf'}
            )
            self.assertSetEqual(
                {d for d in dirs},
                {b'hello'},
            )

    def test_listdir_not_found(self):
        with self.assertRaises(requests.exceptions.HTTPError) as e:
            self.storage.listdir('_this_dir_does_not_exist/')

        self.assertEqual(e.exception.response.status_code, 404)


class TestListdirMethodNotConfigured(TestBase):

    def test_listdir_raises_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.storage.listdir('testdir')
