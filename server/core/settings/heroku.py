import django_heroku

from .base import *

DEBUG = bool(int(os.environ.get('DEBUG', 1)))

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

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

# Activate Django-Heroku.
django_heroku.settings(locals())
