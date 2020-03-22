Configuration
=============

Base settings
-------------

First of all, you need set the your WebDAV server url (``WEBDAV_URL`` setting) and public read-only public url of this if there (``WEBDAV_PUBLIC_URL`` setting)

.. code:: python

    # settings.py

    WEBDAV_URL = "https://my-internal-webdav-server.example.com"
    WEBDAV_PUBLIC_URL = "http://my-awesome-public-webdav-server.example.com"


If you want use HTTP Basic authorization to WebDAV access, you can specify your credentials like that:

.. code:: python

    WEBDAV_URL = 'http://johndoe:secret@my-internal-webdav-server.example.com'


Second, set the ``django_webdav_storage.storage.WebDavStorage`` storage class as default storage class:

.. code:: python

    DEFAULT_FILE_STORAGE = 'django_webdav_storage.storage.WebDavStorage'

If your webdav backend can't recursively create path,  set the ``WEBDAV_RECURSIVE_MKCOL`` variable to ``True`` (please pay attention: `nginx can do this <http://nginx.org/en/docs/http/ngx_http_dav_module.html#create_full_put_path>`_):


.. code::  python

    WEBDAV_RECURSIVE_MKCOL = True    # *NOT* required for nginx!

.. attention::

    The ``WEBDAV_RECURSIVE_MKCOL`` setting must be ``False`` if you use nginx as WebDAV service since ``nginx`` allows you automatically create full path to uploaded file when ``create_full_put_path`` is ``on``.


List support in nginx
---------------------

If you use **nginx** as WebDAV server and want to enable storage directory listing, set the ``WEBDAV_LISTING_BACKEND`` option to:

.. code:: python

    WEBDAV_LISTING_BACKEND = 'django_webdav_storage.listing.nginx_autoindex'

Autoindex feature must be enabled in your nginx configuration for application servers (see example below). Be careful! Allowing autoindex for any user may lead to security and performance issues.

Also, you may specify path to other function with the following interface:

.. code:: python

    def listdir(storage_object, path_string):
        return dirs_list, files_list
