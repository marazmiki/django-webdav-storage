# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
import tempfile
from django import test
from django.core.files.base import ContentFile
from django_webdav_storage.storage import WebDavStorage
from django.utils import six
from django.core.files.uploadedfile import (
    InMemoryUploadedFile, TemporaryUploadedFile,
)
import uuid
import os


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


class TestOverrideSettings(object):
    """
    Test cases for setting overrides
    """
    setting = ''
    method = ''
    value = None

    def test_override_value(self):
        value = self.value or 'new value'

        with self.settings(**{self.setting: value}):
            self.assertEquals(first=value,
                              second=getattr(self.storage, self.method)())


class TestSaveMethod(TestBase):

    def _make_simplefile(self, filename, content):
        fileobj = tempfile.NamedTemporaryFile()
        fileobj.write(content)
        fileobj.flush()
        return fileobj

    def _make_memfile(self, filename, content):
        return InMemoryUploadedFile(
            file=six.StringIO(content),
            field_name='test_field',
            name='_save_new_file.txt',
            content_type='text/plain',
            size=0,
            charset='utf8',
        )

    def _make_tempfile(self, filename, content):
        fileobj = TemporaryUploadedFile(
            name=filename + ".tempfile",
            content_type='text/plain',
            size=0,
            charset='utf8',
        )
        fileobj.write(content)
        fileobj.flush()
        return fileobj

    def test_save_simplefile_ok(self):
        filename = self.session_id + '_save_new_file.txt'
        content = 'test content one'

        fileobj = self._make_simplefile(filename, content)
        self.storage.save(filename, fileobj)
        with self.storage.open(filename) as f:
            self.assertEqual(f.read(), content)

    def test_save_simplefile_seeked_ok(self):
        filename = self.session_id + '_save_new_memsekfile.txt'
        content = 'test content one'

        fileobj = self._make_simplefile(filename, content)
        fileobj.seek(3)

        self.storage.save(filename, fileobj)
        with self.storage.open(filename) as f:
            self.assertEqual(f.read(), content)

    def test_save_memoryfile_ok(self):
        filename = self.session_id + '_save_new_file.txt'
        content = 'test content one'

        fileobj = self._make_memfile(filename, content)
        self.storage.save(filename, fileobj)
        with self.storage.open(filename) as f:
            self.assertEqual(f.read(), content)

    def test_save_tempfile_ok(self):
        filename = self.session_id + '_save_new_file.txt'
        content = 'test content'
        fileobj = self._make_tempfile(filename, content)
        self.storage.save(filename, fileobj)

        with self.storage.open(filename) as f:
            self.assertEqual(f.read(), content)

    def test_save_memoryfile_seeked_ok(self):
        filename = self.session_id + '_save_new_file.txt'
        content = 'test content one'

        fileobj = self._make_memfile(filename, content)
        fileobj.seek(3)

        self.storage.save(filename, fileobj)
        with self.storage.open(filename) as f:
            self.assertEqual(f.read(), content)

    def test_save_tempfile_seeked_ok(self):
        filename = self.session_id + '_save_new_file.txt'
        content = 'test content'
        fileobj = self._make_tempfile(filename, content)
        fileobj.seek(4)

        self.storage.save(filename, fileobj)

        with self.storage.open(filename) as f:
            self.assertEqual(f.read(), content)


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


class TestSizeMethod(TestBase):
    """
    Tests for `url` storage method
    """
    def test_size_for_non_existing_file(self):
        def raise_exception():
            self.storage.size(self.session_id + '_non_exists.txt')
        self.assertRaises(IOError, raise_exception)

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


class TestOpenMethod(TestBase):
    """
    Tests for `_open` storage method
    """
    def test_get_binary_file(self):
        with self.existing_file('empty.gif', content=EMPTY_GIF) as f:
            content = self.storage._open(f.filename, 'rb')
            self.assertEquals(first=EMPTY_GIF,
                              second=content.read())

    def test_get_text_mode(self):
        if six.PY3:
            self.skipTest('Does not work in py3')

        with self.existing_file('file.txt', content=LAZY_FOX) as f:
            content = self.storage._open(f.filename, 'r')
            self.assertEquals(first=LAZY_FOX,
                              second=content.read())


# class TestGetContainerNameMethod(TestOverrideSettings, TestBase):
#    """
#    Tests for `get_container_method` storage method
#    """
#    setting = 'SELECTEL_CONTAINER_NAME'
#    method = 'get_container_name'

    # def mount_requests_adapter(self, prefix, adapter):
    # *def get_base_url(self):

    # def _name(self, name):
    # def _open(self, name, mode='rb'):
    # def _save(self, name, content):
