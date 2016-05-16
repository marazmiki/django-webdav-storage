Requirements
============

* Python ``2.7+``, ``3.4+``, ``3.5+``.
* Django framework version ``1.7+``
* Awesome `python-requests <http://docs.python-requests.org/en/master/>`_ library



.. attention::

    In python 3.x ``ContentFile`` with text mode content (not binary one) will causes ``TypeError`` due `requests <http://docs.python-requests.org/en/master/>`_ restrictions.


Installation
============

You can install the latest stable version of ``django-webdav-storage`` from `PyPI <https://pypi.python.org>`_ within ``pip`` command: ::

    $ pip install django-webdav-storage

or ``easy_install`` one: ::

    $ easy_install django-webdav-storage

If you want install developer version, please use ``pip``: ::

    $ pip install -e git+github.com/marazmiki/django-webdav-storage.git#egg=django-webdav-storage

All dependencies will be installed automatically
