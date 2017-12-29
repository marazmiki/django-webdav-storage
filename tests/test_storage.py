from django_webdav_storage.storage import WebDavStorage


def test_get_base_url_trailing_slashes(settings):
    settings.WEBDAV_PUBLIC_URL = None
    storage = WebDavStorage()

    assert storage.webdav_url == storage.public_url
