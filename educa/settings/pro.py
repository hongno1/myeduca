from .base import *

DEBUG =False

ADMINS = {
    ('ADMIN', 'email@mydomain.com'),
}

ALLOWED_HOSTS = ['educaproject.com', 'www.educaproject.com']

import pymysql
pymysql.install_as_MySQLdb()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'educa',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '',
        'PORT': '3306',
    }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True

