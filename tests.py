#!/usr/bin/env python
# coding: utf-8

from django.conf import settings
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


settings.configure(
    TEST_RUNNER='django.test.runner.DiscoverRunner',
    ROOT_URLCONF='domains.tests.urls',
    INSTALLED_APPS=(
        'django_webdav_storage',
    ),
    MIDDLEWARE_CLASSES=(
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
    ),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':MEMORY:'
        }
    },
    WEBDAV_URL=os.getenv('WEBDAV_URL', 'http://127.0.0.1/'),
    WEBDAV_PUBLIC_URL=os.getenv('WEBDAV_PUBLIC_URL', 'http://127.0.0.1/'),
)


def main():
    from django.test.utils import get_runner
    import django

    if hasattr(django, 'setup'):
        django.setup()

    find_pattern = 'django_webdav_storage'
    failfast = os.getenv('FAILFAST')

    test_runner = get_runner(settings)(verbosity=2,
                                       interactive=True,
                                       failfast=failfast)
    failed = test_runner.run_tests([find_pattern])
    sys.exit(failed)


if __name__ == '__main__':
    main()
