"""
A django-webdav-storage example project settings file.

Most of the settings here are default Django ones and no need inspect it, so
you can skip all this stuff and jump to line #80

"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=5clr&si(d2*@9%1_s%@-&iny2e3tj*lp8%m739yin1v8ge_xc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'example_proj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'example_proj.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

#
# Settings related with `django-webdav-storage`
#

# We should add the "django_webdav_storage" to INSTALLED_APPS to
# make `runwsgidav` management command available.
INSTALLED_APPS += [
    'django_webdav_storage',
    'example_app.apps.ExampleAppConfig',
]

DEFAULT_FILE_STORAGE = 'django_webdav_storage.storage.WebDavStorage'

#
# ``WEBDAV_URL``
#
# A URL of WebDAV server.
#
# When a file is saved using the storage interface, Django'll
# perform WebDAV HTTP requests to this URL. Keep in mind, this
# address *MUST BE SECRET* and/or have limited access by means
# of IP address whitelist or login/password.
#
# By the way,  if you're using an HTTP-Basic Authorization to WebDAV access,
# you can specify login and password directly in the address, like
# that:
#
#       http://username:password@web.dav.server.com:8080/
#
# And a bit about a trailing slash here: whatever ;)
#
WEBDAV_URL = 'http://127.0.0.1:8080/'

#
# ``WEBDAV_PUBLIC_URL``
#
# A public endpoint where uploaded files are accessible.
#
# As said above, WEBDAV_URL must be a secret. And to give end-user
# access to file and don't reveal a secret URL, you have to specify a
# public URL with read-only
#
# If by some reasons you don't specified it, value of ``WEBDAV_URL`` will
# be used instead. Be careful here!
#
WEBDAV_PUBLIC_URL = WEBDAV_URL

#
# ``WEBDAV_RECURSIVE_MKCOL``
#
# Whether django-WebDAV-storage should make a directory tree (it
# called a "collection" in WebDAV terms) before uploading a file.
#
# When saving a file in a directory (e.g. my/music/django.mp3), the last
# one should exist. Some WebDAV servers (e.g. nginx does) can do it
# automatically if the target directory is absent.
#
# If your WebDAV backend doesn't support this feature, you should send a
# request to "my" directory creation, then - "my/music" one and so on, and
# only after that, you can upload the file.
#
# It's more reliable option, but it's a bit slower as causes a
# sequence of HTTP MKCOL queries.
#
WEBDAV_RECURSIVE_MKCOL = True

#
# ``WEBDAV_LISTING_BACKEND``
#
# By default, you couldn't view a list of directory files and
# subdirectories; but if WebDAV backend supports directory indexing,
# we could parse it for you :)
#
# Currently supports nginx and wsgidav backends
#
WEBDAV_LISTING_BACKEND = 'django_webdav_storage.listing.wsgidav_autoindex'

#
# Settings for ``./manage.py run_wsgidav`` command
#

# A default port for developer wsgi server
WEBDAV_WSGIDAV_PORT = 8080

# A directory
WEBDAV_WSGIDAV_ROOT = os.path.join(BASE_DIR, 'webdav_storage', 'media')
