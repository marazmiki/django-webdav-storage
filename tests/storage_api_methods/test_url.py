import os
import pytest
from django_webdav_storage import storage


@pytest.fixture
def url():
    return os.getenv('WEBDAV_PUBLIC_URL', 'http://127.0.0.1')


@pytest.mark.parametrize(
    argnames='appendix, arg',
    argvalues=[
        ('/index.html', 'index.html'),
    ],
)
def test_url(webdav_storage, appendix, arg):
    assert webdav_storage.url('').rstrip('/') + appendix \
           == webdav_storage.url(arg)


@pytest.mark.parametrize(
    argnames='appendix',
    argvalues=[
        '',
        '/',
        '////'
    ],
    ids=[
        'no trailing slashes',
        'one trailing slash',
        'multiple trailing slashes',
    ]
)
def test_get_base_url_trailing_slashes(url, settings, appendix):
    settings.WEBDAV_PUBLIC_URL = url + appendix
    webdav_storage = storage.WebDavStorage()
    assert url == webdav_storage.url('')
