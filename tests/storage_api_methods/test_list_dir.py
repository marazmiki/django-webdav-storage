import os
import uuid
import pytest
import requests.exceptions
from django_webdav_storage import storage


def test_listdir_raises_not_implemented(settings):
    del settings.WEBDAV_LISTING_BACKEND

    webdav_storage = storage.WebDavStorage()

    with pytest.raises(NotImplementedError):
        webdav_storage.listdir('testdir')


def test_listdir_not_found(webdav_storage):
    with pytest.raises(requests.exceptions.HTTPError):
        webdav_storage.listdir('_this_dir_does_not_exist/')


@pytest.mark.parametrize(
    argnames='var_name, expected_items',
    argvalues=[
        ('files', {b'file.img', b'hello.pdf'}),
        ('dirs', {b'hello'}),
    ],
    ids=['files', 'directories']
)
def test_listdir_works(webdav_storage, create_file, settings,
                       var_name, expected_items):
    prefix = '{0}/listdir'.format(uuid.uuid4())
    root = 'test-list/'

    for f in ['file.img', 'hello.pdf', 'hello/image.png', 'hello/text.txt']:
        create_file(root + f, prefix=prefix)

    bla = webdav_storage.listdir(os.path.join(prefix, root))
    dirs, files = bla

    assert {_ for _ in locals()[var_name]} == expected_items
