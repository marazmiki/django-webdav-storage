Change log
==========


1.x
---

1.1
~~~

* The oldest supported Python version is ``3.6``;
* Added support for ``Django 4.x``;
* Using github actions instead of Travis;


1.0.0
~~~~~~


* Using ``poetry`` in the development;
* Using ``py.test`` instead of unittest-based Django test framework;
* Testing locally in all the supported environments with `tox <https://tox.readthedocs.io/en/latest/>`_
* Added support for Python ``3.6``, ``3.7`` and ``3.8``;
* Dropped support for Python ``3.2``, ``3.3`` and ``3.4``
* Added support for Django ``1.11``, ``2.x`` and ``3.x``;
* Dropped support of all the older Django versions;
* Added the ``run_wsgidav`` command that creates a developer WebDAV server;
* Added an example project;
* Improved documentation;


0.6x
----

0.6.1
~~~~~

* Cleanup code, remove unused code — thanks to Matvei Kroglov

0.6
~~~

* Add directory listing feature (if webdav server supports it) — thanks to Matvei Kroglov

0.5x
----

0.5
~~~

* Chunked upload support — thanks to Matvei Kroglov


0.4x
----

0.4.2
~~~~~

* Update django versions


0.4.1
~~~~~

* Update django versions

0.4
~~~

* Updated head django versions;
* Support of Django 1.8x;
* Explicit directory tree creation (MKCOL) now os optional — thanks to Dmitriy Narkevich
* Added missed self.webdav wrapper for MKCOL request

0.3x
----

0.3
~~~

* Updated head django versions;
* Explicit directory tree creation (MKCOL) — thanks to Richard Lander;
* Fix set_public_url and set_webdav_url method names — thanks to fuxter;
* Added AUTHORS.rst and CHANGELOG.rst files

0.2x
----

0.2
~~~

* Updated head Django versions.


0.1x
----

0.1
~~~

* Initial release.
