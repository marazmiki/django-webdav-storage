def test_get_zero_length_str(webdav_storage, create_file):
    file = create_file('zero.txt', content='')
    content = webdav_storage._open(file, 'r')
    assert content.read() == b''


def test_get_zero_length_byte(webdav_storage, create_file):
    file = create_file('zero.txt', content=b'')

    content = webdav_storage._open(file, 'r')
    assert content.read() == b''


def test_get_binary_file(webdav_storage, create_file, empty_gif):
    file = create_file('empty.gif', content=empty_gif)
    assert webdav_storage._open(file, 'rb').read() == empty_gif


def test_get_text_mode(webdav_storage, create_file, lazy_fox):
    file = create_file('file.txt', content=lazy_fox)
    assert webdav_storage._open(file, 'r').read() == lazy_fox.encode('UTF-8')
