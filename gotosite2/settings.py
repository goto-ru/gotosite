"""
Django settings for gotosite2 project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iwz6w2xk$e6tn)ka2d3ugi26*f^9_slx40oadsg^8=#4v=zg^='

# SECURITY WARNING: don't run with debug turned on in production!
LOGIN_URL = '/login'
ALLOWED_HOSTS = []

# Application definition
from django.contrib.messages import constants

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'goto',
    'nested_inline',
    'django_jinja',
    'filer',
    'easy_thumbnails',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.vk',
]
SITE_ID = 2
MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'
MESSAGE_TAGS = {
    constants.ERROR: 'alert-danger',
    constants.INFO: 'alert-info'
}

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gotosite2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'templates', 'allauth')],
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
    # {
    #     'BACKEND': 'django_jinja.backend.Jinja2',
    #     'DIRS': [os.path.join(BASE_DIR, 'allauth')],
    #     'APP_DIRS': True,
    #     'OPTIONS': {
    #         "match_extension": ".html",
    #         # 'context_processors': [
    #         #     'django.template.context_processors.debug',
    #         #     'django.template.context_processors.request',
    #         #     'django.contrib.auth.context_processors.auth',
    #         #     'django.contrib.messages.context_processors.messages',
    #         # ],
    #     },
    # },
]
LOGIN_REDIRECT_URL = '/'
SOCIALACCOUNT_QUERY_EMAIL = True

AUTHENTICATION_BACKENDS = (

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend'
)

DATE_FORMAT = 'd.m.Y'

WSGI_APPLICATION = 'gotosite2.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

env = os.getenv('ENV', 'debug')
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': '5432',

    }
}
DEBUG = True

if env == 'debug':
    from .private_settings.debug_settings import *

    DATABASES['default']['HOST'] = '127.0.0.1'
else:
    from .private_settings.production_settings import *

    ALLOWED_HOSTS = ['localhost']

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'
STATIC_ROOT = 'static/'
