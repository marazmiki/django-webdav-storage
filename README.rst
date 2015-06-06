=====================
django-webdav-storage
=====================


.. image:: https://badge.fury.io/py/django-webdav-storage.png
    :target: http://badge.fury.io/py/django-webdav-storage
    :alt:

.. image:: https://travis-ci.org/marazmiki/django-webdav-storage.png?branch=master
    :target: https://travis-ci.org/marazmiki/django-webdav-storage
    :alt: Travis CI build status

.. image:: https://coveralls.io/repos/marazmiki/django-webdav-storage/badge.png?branch=master
    :target: https://coveralls.io/r/marazmiki/django-webdav-storage?branch=master
    :alt: Code coverage percentage

.. image:: https://pypip.in/d/django-webdav-storage/badge.png
    :target: https://pypi.python.org/pypi/django-webdav-storage
    :alt: Latest version on PyPI

.. image:: https://pypip.in/wheel/django-webdav-storage/badge.svg
    :target: https://pypi.python.org/pypi/django-webdav-storage/
    :alt: Wheel Status

.. image:: https://pypip.in/py_versions/django-webdav-storage/badge.png
    :target: https://pypi.python.org/pypi/django-webdav-storage/
    :alt: Supported Python versions

This application allows you to easily save media and static files into a webdav storage.

Dependencies
------------

* `requests <http://docs.python-requests.org/en/latest/>`_ library

Installation
------------

1. Installing the package

.. code:: bash

    pip install django-webdav-storage

2. Pick the webdav server url in `WEBDAV_URL` and `WEBDAV_PUBLIC_URL`:

.. code:: python

    WEBDAV_URL = 'http://webdav.example.com/',
    WEBDAV_PUBLIC_URL = 'http://webdav.example.com/'

If you want use HTTP Basic authorization to webdav access, you can specify
your credentials:

.. code:: python

    WEBDAV_URL = 'http://johndoe:secret@webdav.example.com/'


3. Set the webdav storage class as default:

.. code:: python

    DEFAULT_FILE_STORAGE = 'django_webdav_storage.storage.WebDavStorage'

4. If your webdav backend can't recursively create path (e.g. `nginx can do this <http://nginx.org/en/docs/http/ngx_http_dav_module.html#create_full_put_path>`_, while apache can't), set the `WEBDAV_RECURSIVE_MKCOL` variable to `True`:

.. code:: python

    WEBDAV_RECURSIVE_MKCOL = True

5. If you use nginx as webdav server and want to enable storage directory listing, set the WEBDAV_LISTING_BACKEND option to:

.. code:: python

    WEBDAV_LISTING_BACKEND = 'django_webdav_storage.listing.nginx_autoindex'

Autoindex feature must be enabled in your nginx configuration for application servers (see example below). Be careful! Allowing autoindex for any user may lead to security and performance issues.

Also, you may specify path to other functions with the following interface:

.. code:: python

    def listdir(storage_object, path_string):
        return dirs_list, files_list


The nginx webdav configuration example
--------------------------------------

.. code:: nginx

    # Public readonly media server.
    server {
        listen 80;
        charset        utf-8;
        server_tokens  off;
        server_name    media.example.com;

        access_log     /var/log/nginx/media_access.log;
        error_log      /var/log/nginx/media_error.log;

        root           /usr/share/nginx/webdav;

    }

    # WebDAV server
    server {
        listen 80;
        charset        utf-8;
        server_tokens  off;
        server_name    webdav.example.com;

        access_log     /var/log/nginx/webdav_access.log;
        error_log      /var/log/nginx/webdav_error.log;

        root           /usr/share/nginx/webdav;

        client_max_body_size    10m;
        client_body_temp_path   /tmp;
        create_full_put_path    on;
        autoindex               on;

        dav_methods             PUT DELETE MKCOL COPY MOVE;
        dav_access              user:rw   group:r   all:r;

        satisfy                 any;

        allow                   127.0.0.1/32;
        deny                    all;

        auth_basic              'My WebDAV area';
        auth_basic_user_file    /usr/share/nginx/.htpasswd;
    }



Caveats
-------

* In python 3.x ``ContentFile`` with text mode content (not the binary one) will cause ``TypeError`` due to ``requests`` restrictions.
