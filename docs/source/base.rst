Requirements
============

* The package works both on Python 2.7 and 3.5+.
* Required `Django <https://djangoproject.com/>`_ version is ``1.11+``. The ``2.x`` and ``3.x`` branches are also supported.
* The `requests <http://docs.python-requests.org/en/master/>`_ library.

.. attention::

    In python 3.x,  ``ContentFile`` with text mode content (not binary one) will causes ``TypeError`` due `requests <http://docs.python-requests.org/en/master/>`_ restrictions.

Installation
============

You can install the latest stable version of ``django-webdav-storage`` from `PyPI <https://pypi.org>`_ within ``pip`` command:

.. code:: bash

    $ pip install django-webdav-storage

Of course, you also can use a development version:

.. code:: bash

    $ pip install -e git+github.com/marazmiki/django-webdav-storage.git#egg=django-webdav-storage

All dependencies will be installed automatically
