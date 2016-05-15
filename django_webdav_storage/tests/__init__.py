# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from django import test
from django.core.files.base import ContentFile
from django_webdav_storage.storage import WebDavStorage
import uuid


override_settings = getattr(test, 'override_settings',
                            test.utils.override_settings)


LAZY_FOX = 'The *quick* brown fox jumps over the lazy dog'
EMPTY_GIF = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\xf0\x01\x00' \
            b'\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x0a\x00\x00' \
            b'\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02' \
            b'\x44\x01\x00\x3b'


class ExistingFile(object):
    def __init__(self, test_case, fn, cnt, file_class=ContentFile):
        self.test = test_case
        self.filename = self.test.session_id + '_' + fn
        self.content = file_class(cnt)

    def __enter__(self):
        self.test.storage.save(self.filename, self.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.test.storage.delete(self.filename)


class TestBase(test.TestCase):
    """
    Base test class
    """

    def setUp(self):
        self.storage = WebDavStorage()
        self.session_id = uuid.uuid4().hex

    def existing_file(self, filename, content=''):
        return ExistingFile(self, filename, content)
