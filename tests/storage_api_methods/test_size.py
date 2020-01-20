import pytest


def test_error_when_trying_to_get_size_of_non_existing_file(webdav_storage):
    with pytest.raises(IOError):
        webdav_storage.size('non-exists.txt')


def test_zero_size_file(webdav_storage, create_file):
    file = create_file('zero_size.txt', content='')
    assert webdav_storage.size(file) == 0


def test_size_binary_file(webdav_storage, create_file, empty_gif):
    file = create_file('empty.gif', content=empty_gif)
    assert webdav_storage.size(file) == len(empty_gif)


def test_size_text_file(webdav_storage, create_file, lazy_fox):
    file = create_file('README.md', content=lazy_fox)
    assert webdav_storage.size(file) == len(lazy_fox)
