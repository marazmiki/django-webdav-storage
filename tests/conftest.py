import os
import uuid
import pytest


def pytest_configure():
    from django.conf import settings

    WEBDAV_URL = os.getenv('WEBDAV_URL', 'http://127.0.0.1:8080/')
    WEBDAV_PUBLIC_URL = os.getenv('WEBDAV_PUBLIC_URL',
                                  'http://127.0.0.1:8080/')

    settings.configure(
        INSTALLED_APPS=['django_webdav_storage'],
        MIDDLEWARE_CLASSES=['django.middleware.common.CommonMiddleware'],
        MIDDLEWARES=['django.middleware.common.CommonMiddleware'],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':MEMORY:'
            }
        },
        WEBDAV_URL=WEBDAV_URL,
        WEBDAV_PUBLIC_URL=WEBDAV_PUBLIC_URL,
        WEBDAV_RECURSIVE_MKCOL=True,
        WEBDAV_LISTING_BACKEND=(
            'django_webdav_storage.listing.wsgidav_autoindex'
        )
    )


@pytest.fixture
def webdav_storage(settings):
    "Creates a WebDavStorage instance for test purposes"
    from django_webdav_storage import storage
    return storage.WebDavStorage()


@pytest.fixture
def create_file(webdav_storage):
    """
    Creates a file with a unique prefix in the WebDAV storage and
    then deletes the file after the test finished
    """
    from django.core.files.base import ContentFile
    from django.utils import six

    def inner(filename, content=b'', prefix=''):
        if all((six.PY3, isinstance(content, six.text_type))):
            content = content.encode('UTF-8')

        col = str(uuid.uuid4())
        key = os.path.join(prefix.lstrip('/') or col, filename)

        webdav_storage.save(key, ContentFile(content, key))

        return key

        webdav_storage.delete(key)
    return inner


@pytest.fixture
def empty_gif():
    """A 1x1 GIF image"""
    return (
        b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\xf0\x01\x00'
        b'\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x0a\x00\x00'
        b'\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02'
        b'\x44\x01\x00\x3b'
    )


@pytest.fixture
def lazy_fox():
    """Just a text string"""
    return 'The *quick* brown fox jumps over the lazy dog'


class SettingsWrapper:
    """
    Stolen from the awesome pytest-django.
    """

    _to_restore = []

    def __delattr__(self, attr):
        from django.test import override_settings
        override = override_settings()
        override.enable()
        from django.conf import settings
        delattr(settings, attr)

        self._to_restore.append(override)

    def __setattr__(self, attr, value):
        from django.test import override_settings

        override = override_settings(**{
            attr: value
        })

        override.enable()
        self._to_restore.append(override)

    def __getattr__(self, item):
        from django.conf import settings
        return getattr(settings, item)

    def finalize(self):
        for override in reversed(self._to_restore):
            override.disable()
        del self._to_restore[:]


@pytest.fixture
def settings():
    wrapper = SettingsWrapper()
    yield wrapper
    wrapper.finalize()
