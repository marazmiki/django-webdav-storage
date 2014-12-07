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

This application allows you easily save media and static files into webdav storage.

Dependencies
------------

* `requests <http://docs.python-requests.org/en/latest/>`_ library

Installation
------------

1. Install the package

.. code:: bash

    pip install django-webdav-storage

2. Pick the webdav server url in `WEBDAV_URL` and `WEBDAV_PUBLIC_URL`:

.. code:: python

    WEBDAV_URL = 'http://webdav.example.com/',
    WEBDAV_PUBLIC_URL = 'http://webdav.example.com/'

If you want use HTTP Basic authorization to webdav access, you can specify
your credentials like that:

.. code:: python

    WEBDAV_URL = 'http://johndoe:secret@webdav.example.com/'


3. Set the webdav storage class as default:

.. code:: python

    DEFAULT_FILE_STORAGE = 'django_webdav_storage.storage.WebDavStorage'


WebDAV nginx example
--------------------

.. code:: nginx

    server {
        listen 80;
        charset        utf-8;
        server_tokens  off;
        server_name    webdav.example.com;

        access_log     /var/log/nginx/webdav_access.log;
        error_log      /var/log/nginx/webdav_error.log;

        root           /usr/share/nginx/webdav;

        location / {
            client_max_body_size    10m;
            client_body_temp_path   /tmp;
            create_full_put_path    on;

            dav_methods             PUT DELETE MKCOL COPY MOVE;
            dav_access              user:rw   group:r   all:r;

            satisfy  any;

            limit_except GET {
                allow           127.0.0.1/32;
                deny            all;
                auth_basic 'My WebDAV area';
                auth_basic_user_file /usr/share/nginx/.htpasswd;
            }
        }
    }



Caveats
-------

* In python 3.x ``ContentFile`` with text mode content (not binary one) will causes ``TypeError`` due ``requests`` restrictions
