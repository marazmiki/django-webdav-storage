import os
import requests
from django.conf import settings
from django.core.files.storage import Storage as StorageBase
from django.core.files.base import ContentFile
from django.utils.module_loading import import_string


def setting(name, default=None):
    return getattr(settings, name, default)


class WebDavStorage(StorageBase):
    def __init__(self, **kwargs):
        self.requests = self.get_requests_instance(**kwargs)
        self.webdav_url = self.set_webdav_url(**kwargs)
        self.public_url = self.set_public_url(**kwargs)
        self.listdir = self.set_listdir(**kwargs)

        if not self.webdav_url:
            raise NotImplementedError('Please define webdav url')
        if not self.public_url:
            self.public_url = self.webdav_url

    def set_webdav_url(self, **kwargs):
        return kwargs.get('webdav_url') or setting('WEBDAV_URL')

    def set_public_url(self, **kwargs):
        return kwargs.get('public_url') or setting('WEBDAV_PUBLIC_URL')

    def set_listdir(self, **kwargs):
        dottedpath = kwargs.get(
            'listing_backend',
        ) or setting(
            'WEBDAV_LISTING_BACKEND'
        )

        if dottedpath is None:
            return self.listdir

        listdir = import_string(dottedpath)
        return lambda path: listdir(self, path)

    def listdir(self, path):
        raise NotImplementedError(
            'Listing backend not configured. '
            'Please set WEBDAV_LISTING_BACKEND '
            'configuration option.'
        )

    def get_requests_instance(self, **kwargs):
        return requests.Session()

    def webdav(self, method, name, *args, **kwargs):
        url = self.get_webdav_url(name)
        method = method.lower()
        response = getattr(self.requests, method)(url, *args, **kwargs)
        print('webdav ', method, url)
        response.raise_for_status()

        return response

    def get_public_url(self, name):
        return self.public_url.rstrip('/') + '/' + name.lstrip('/')

    def get_webdav_url(self, name):
        return self.webdav_url.rstrip('/') + '/' + name.lstrip('/')

    def _open(self, name, mode='rb'):
        content = self.webdav('GET', name).content
        return ContentFile(content, name)

    def _save(self, name, content):
        headers = None

        if setting('WEBDAV_RECURSIVE_MKCOL', False):
            self.make_collection(name)

        if hasattr(content, 'temporary_file_path'):
            with open(content.temporary_file_path(), 'rb') as f:
                self.webdav(method='PUT',
                            name=name,
                            data=f,
                            headers=headers
                            )
        else:
            content.file.seek(0)
            self.webdav(method='PUT',
                        name=name,
                        data=content.file,
                        headers=headers
                        )
        return name

    def make_collection(self, name):
        coll_path = self.webdav_url

        for directory in name.split('/')[:-1]:
            col = os.path.join(coll_path, directory)

            resp = self.requests.head(col)
            if resp.status_code not in (200, ):
                resp = self.requests.request('MKCOL', col)
                resp.raise_for_status()

            coll_path = os.path.join(coll_path, directory)

    def delete(self, name):
        try:
            self.webdav('DELETE', name)
        except requests.HTTPError:
            pass

    def exists(self, name):
        try:
            self.webdav('HEAD', name)
        except requests.exceptions.HTTPError:
            return False
        else:
            return True

    def size(self, name):
        try:
            return int(self.webdav('HEAD', name).headers['content-length'])
        except (ValueError, requests.exceptions.HTTPError):
            raise IOError('Unable get size for %s' % name)

    def url(self, name):
        return self.get_public_url(name)

    def get_base_url(self):
        return self.url('').rstrip('/')


class WebDavStaticStorage(WebDavStorage):
    base_url = setting('WEBDAV_STATIC_BASE_URL')
