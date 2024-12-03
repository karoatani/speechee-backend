import os
import dj_database_url
from .settings import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
    ),
    'ENGINE': 'django.db.backends.postgresql',
}