import io
import tempfile
import uuid

import pytest
from django.core.files import uploadedfile


@pytest.fixture
def file_id():
    return str(uuid.uuid4())


@pytest.fixture
def simple_file():
    def inner(filename, content):
        fp = tempfile.NamedTemporaryFile()
        fp.write(content)
        fp.flush()
        return fp
    return inner


@pytest.fixture
def in_memory_file():
    def inner(filename, content):
        return uploadedfile.InMemoryUploadedFile(
            file=io.BytesIO(content),
            field_name='test_field',
            name='_save_new_file.txt',
            content_type='text/plain',
            size=0,
            charset='utf8'
        )
    return inner


@pytest.fixture
def temporary_uploaded_file():
    def inner(filename, content):
        fp = uploadedfile.TemporaryUploadedFile(
            name=filename + ".tempfile",
            content_type='text/plain',
            size=0,
            charset='utf8',
        )
        fp.write(content)
        fp.flush()
        return fp
    return inner


parametrize = pytest.mark.parametrize(
    argnames='fixture_name',
    argvalues=[
        'simple_file',
        'in_memory_file',
        'temporary_uploaded_file',
    ]
)


@parametrize
def test_save_fileobj(webdav_storage, request, file_id, fixture_name):
    request.getfixturevalue(fixture_name)

    filename = 'save_new_file_{0}.txt'.format(file_id)
    content = b'test content one'

    fileobj = request.getfixturevalue(fixture_name)(filename, content)
    webdav_storage.save(filename, fileobj)

    with webdav_storage.open(filename) as f:
        assert f.read() == content


@parametrize
def test_save_seeked_fileobj(webdav_storage, request, file_id, fixture_name):
    request.getfixturevalue(fixture_name)

    filename = 'save_new_file_{0}.txt'.format(file_id)
    content = b'test content one'

    fileobj = request.getfixturevalue(fixture_name)(filename, content)
    fileobj.seek(3)

    webdav_storage.save(filename, fileobj)

    with webdav_storage.open(filename) as f:
        assert f.read() == content


def test_no_mkcol(settings, webdav_storage, file_id, simple_file):
    settings.WEBDAV_RECURSIVE_MKCOL = False

    filename = 'save_new_file_{0}.txt'.format(file_id)
    content = b'Test'

    fp = simple_file(filename, content)
    webdav_storage.save(filename, fp)
