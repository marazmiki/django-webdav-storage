import uuid


def test_exists_returns_false_when_the_file_does_not_exist(webdav_storage):
    non_existing_file = '{0}/non-exist.txt'.format(uuid.uuid4())
    assert not webdav_storage.exists(non_existing_file)


def test_exists_returns_true_when_the_file_exists(webdav_storage, create_file):
    existing_file = create_file('exists.txt', 'Yup, it\'s exists!')
    assert webdav_storage.exists(existing_file)
