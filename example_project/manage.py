#!/usr/bin/env python

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example_proj.settings")
    try:
        from django.core.management import execute_from_command_line

    # Although the example project made based on Django 2.x template, we also
    # would like to use it also in Django 1.x/Python 2.x.

    except ImportError:  # as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )  # from exc
    execute_from_command_line(sys.argv)
