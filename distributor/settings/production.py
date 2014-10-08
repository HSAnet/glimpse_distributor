from distributor.settings.base import *

DEBUG = False

TEMPLATE_DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'glimpse',
        'USER': 'glimpse_services',
        'PASSWORD': "changeme",
        'HOST': '141.82.57.240',
        'PORT': '5432',
    },
}

ALLOWED_HOSTS = ['distributor.measure-it.net']
