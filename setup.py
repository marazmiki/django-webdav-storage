#!/usr/bin/env python
# coding: utf-8

import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test


try:
    from ConfigParser import ConfigParser
except ImportError:
    from configparser import ConfigParser


NAME = 'django-webdav-storage'
ROOT = os.path.realpath(os.path.dirname(__file__))
DESCRIPTION = (
    'This application allows you easily save user-generated and '
    'static files into your own WebDAV storage rather than a local '
    'filesystem, as Django does by default.'
)


config = ConfigParser()
config.read(os.path.join(ROOT, 'setup.cfg'))


class TestCmd(test):
    user_options = [
        ('pytest-args=', 'a', "Arguments to pass to py.test")
    ]

    def initialize_options(self):
        test.initialize_options(self)
        self.pytest_args = ''

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        import shlex
        sys.exit(pytest.main(shlex.split(self.pytest_args)))


def get_version():
    return config.get('bumpversion:bumpversion', 'current_version')


def get_long_description():
    def read(what):
        with open(os.path.join(ROOT, '{0}.rst'.format(what))) as fp:
            return fp.read()
    return '{README}\n'.format(README=read('README'))


setup(name=NAME,
      description=DESCRIPTION,
      author='Mikhail Porokhovnichenko',
      author_email='marazmiki@gmail.com',
      url='https://github.com/marazmiki/django-webdav-storage',
      version=get_version(),
      long_description=get_long_description(),
      packages=find_packages(),
      license='BSD',
      include_package_data=True,
      test_suite='tests',
      install_requires=['django', 'requests'],
      tests_require=[
          'django', 'requests', 'coveralls', 'flake8', 'coverage',
          'pytest', 'pytest-cov',
      ],
      zip_safe=False,
      cmdclass={
          'test': TestCmd,
      },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Framework :: Django',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      ])
