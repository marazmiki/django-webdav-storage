=====================
django-webdav-storage
=====================


.. image:: https://badge.fury.io/py/django-webdav-storage.png
    :target: http://badge.fury.io/py/django-webdav-storage

.. image:: https://travis-ci.org/marazmiki/django-webdav-storage.png?branch=master
    :target: https://travis-ci.org/marazmiki/django-webdav-storage

.. image:: https://coveralls.io/repos/marazmiki/django-webdav-storage/badge.png?branch=master
    :target: https://coveralls.io/r/marazmiki/django-webdav-storage?branch=master

.. image:: https://pypip.in/d/django-webdav-storage/badge.png
    :target: https://pypi.python.org/pypi/django-webdav-storage


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

    WEBDAV_URL='http://webdav.example.com/',
    WEBDAV_PUBLIC_URL='http://webdav.example.com/'

3. Set the webdav storage class as default:

.. code:: python

    DEFAULT_FILE_STORAGE = 'django_webdav_storage.storage.WebDavStorage'


Caveats
-------

* In python 3.x ``ContentFile`` with text mode content (not binary one) will causes ``TypeError`` due ``requests`` restrictions
