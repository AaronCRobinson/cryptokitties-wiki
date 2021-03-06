# -*- coding: utf-8 -*-
"""
Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

from __future__ import unicode_literals

import os

from django.core.urlresolvers import reverse_lazy
from django.utils.crypto import get_random_string

def generate_secret_key(filename):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    with open(filename, "w") as file:
        file.write("SECRET_KEY='{0}'".format(get_random_string(50, chars)))

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
try:
    from .secret_key import SECRET_KEY
except ImportError:
    settings_dir = os.path.abspath(os.path.dirname(__file__))
    generate_secret_key(os.path.join(PROJECT_DIR, 'settings', 'secret_key.py'))
    from .secret_key import SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.humanize',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'sekizai',
    'sorl.thumbnail',
    'django_nyt',
    'wiki',
    'wiki.plugins.macros',
    'wiki.plugins.help',
#    'wiki.plugins.links',
    'wiki.plugins.images',
    'wiki.plugins.attachments',
    'wiki.plugins.notifications',
#    'wiki.plugins.globalhistory',
    'mptt',
]

TEST_RUNNER = 'django.test.runner.DiscoverRunner'


MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

ROOT_URLCONF = 'testproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.request",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "sekizai.context_processors.sekizai",
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'testproject.wsgi.application'


LOGIN_REDIRECT_URL = reverse_lazy('wiki:get', kwargs={'path': ''})


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'db', 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

TIME_ZONE = 'Europe/Rome'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-US'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'

# https://stackoverflow.com/questions/10165638/django-isnt-serving-static-files-getting-404-errors/10165796

WIKI_ANONYMOUS_WRITE = True
WIKI_ANONYMOUS_CREATE = True

# NOTE: potential dangerous
#WIKI_MARKDOWN_SANITIZE_HTML = False

WIKI_MARKDOWN_HTML_ATTRIBUTES = {'a': ['href', 'title', 'class', 'id'], 'abbr': ['title', 'class', 'id'], 'acronym': ['title', 'class', 'id'], 'b': ['class', 'id'], 'blockquote': ['class', 'id'], 'br': ['class', 'id'], 'code': ['class', 'id'], 'dd': ['class', 'id'], 'div': ['class', 'id'], 'dl': ['class', 'id'], 'dt': ['class', 'id'], 'em': ['class', 'id'], 'figcaption': ['class', 'id'], 'figure': ['class', 'id'], 'h0': ['class', 'id'], 'h1': ['class', 'id'], 'h2': ['class', 'id'], 'h3': ['class', 'id'], 'h4': ['class', 'id'], 'h5': ['class', 'id'], 'h6': ['class', 'id'], 'h7': ['class', 'id'], 'hr': ['class', 'id'], 'i': ['class', 'id'], 'img': ['class', 'id', 'src', 'alt', 'width', 'height'], 'li': ['class', 'id'], 'ol': ['class', 'id'], 'p': ['class', 'id'], 'pre': ['class', 'id'], 'span': ['class', 'id'], 'strong': ['class', 'id'], 'sup': ['class', 'id'], 'table': ['class', 'id'], 'tbody': ['class', 'id'], 'td': ['class', 'id'], 'th': ['class', 'id'], 'thead': ['class', 'id'], 'tr': ['class', 'id'], 'ul': ['class', 'id'], 'embed': ['src', 'width', 'height']}

# NOTE: ACR - this does not appear to be working...
WIKI_MARKDOWN_HTML_STYLES = ['float', 'width', 'height', 'clear']

WIKI_MARKDOWN_HTML_WHITELIST = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i', 'li', 'ol', 'strong', 'ul', 'figure', 'figcaption', 'br', 'hr', 'p', 'div', 'img', 'pre', 'span', 'sup', 'table', 'thead', 'tbody', 'th', 'tr', 'td', 'dl', 'dt', 'dd', 'h0', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'embed']


