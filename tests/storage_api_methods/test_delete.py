import os
import uuid


def test_not_failed_when_deleting_a_non_existing_file(webdav_storage):
    non_existing_file = os.path.join(str(uuid.uuid4()), 'non-exists.txt')
    webdav_storage.delete(non_existing_file)


def test_delete_works(webdav_storage, create_file):
    existing_file = create_file('DELETE_ME.txt', 'Please, delete me!')

    assert webdav_storage.exists(existing_file)

    webdav_storage.delete(existing_file)

    assert not webdav_storage.exists(existing_file)
