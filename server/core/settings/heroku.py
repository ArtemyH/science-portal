import django_heroku

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'csportal',
        'USER': 'csportal',
        'PASSWORD': 'csportal',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}

# Activate Django-Heroku.
django_heroku.settings(locals())
