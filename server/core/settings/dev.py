from django.conf import settings

from core.settings.base import *

DEBUG = True

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

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if settings.DEBUG:
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
    INSTALLED_APPS.append('debug_toolbar')
    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": lambda request: True,
    }

try:
    from core.settings.local_settings import *
except ImportError:
    pass
