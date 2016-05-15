# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from django_webdav_storage.tests import TestBase
from django.utils import six
from django.core.files import uploadedfile
import tempfile


class TestSaveMethod(TestBase):

    def _make_simplefile(self, filename, content):
        fileobj = tempfile.NamedTemporaryFile()
        fileobj.write(content)
        fileobj.flush()
        return fileobj

    def _make_memfile(self, filename, content):
        return uploadedfile.InMemoryUploadedFile(
            file=six.BytesIO(content),
            field_name='test_field',
            name='_save_new_file.txt',
            content_type='text/plain',
            size=0,
            charset='utf8',
        )

    def _make_tempfile(self, filename, content):
        fileobj = uploadedfile.TemporaryUploadedFile(
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
        content = six.b('test content one')

        fileobj = self._make_simplefile(filename, content)
        self.storage.save(filename, fileobj)
        with self.storage.open(filename) as f:
            self.assertEqual(f.read(), content)

    def test_save_simplefile_seeked_ok(self):
        filename = self.session_id + '_save_new_memsekfile.txt'
        content = six.b('test content one')

        fileobj = self._make_simplefile(filename, content)
        fileobj.seek(3)

        self.storage.save(filename, fileobj)
        with self.storage.open(filename) as f:
            self.assertEqual(f.read(), content)

    def test_save_memoryfile_ok(self):
        filename = self.session_id + '_save_new_file.txt'
        content = six.b('test content one')

        fileobj = self._make_memfile(filename, content)
        self.storage.save(filename, fileobj)
        with self.storage.open(filename) as f:
            self.assertEqual(f.read(), content)

    def test_save_tempfile_ok(self):
        filename = self.session_id + '_save_new_file.txt'
        content = six.b('test content')
        fileobj = self._make_tempfile(filename, content)
        self.storage.save(filename, fileobj)

        with self.storage.open(filename) as f:
            self.assertEqual(f.read(), content)

    def test_save_memoryfile_seeked_ok(self):
        filename = self.session_id + '_save_new_file.txt'
        content = six.b('test content one')

        fileobj = self._make_memfile(filename, content)
        fileobj.seek(3)

        self.storage.save(filename, fileobj)
        with self.storage.open(filename) as f:
            self.assertEqual(f.read(), content)

    def test_save_tempfile_seeked_ok(self):
        filename = self.session_id + '_save_new_file.txt'
        content = six.b('test content')
        fileobj = self._make_tempfile(filename, content)
        fileobj.seek(4)

        self.storage.save(filename, fileobj)

        with self.storage.open(filename) as f:
            self.assertEqual(f.read(), content)
