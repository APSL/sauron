# -*- coding: utf-8 -*-

from os.path import join

from configurations import Configuration
from django.contrib.messages import constants as messages
from kaio import Options
from kaio.mixins import (CachesMixin, DatabasesMixin, CompressMixin, LogsMixin,
                         PathsMixin, SecurityMixin, DebugMixin, WhiteNoiseMixin)


opts = Options()


class Base(CachesMixin, DatabasesMixin, CompressMixin, PathsMixin, LogsMixin,
           SecurityMixin, DebugMixin, WhiteNoiseMixin, Configuration):
    """
    Project settings for development and production.
    """

    DEBUG = opts.get('DEBUG', True)

    BASE_DIR = opts.get('APP_ROOT', None)
    APP_SLUG = opts.get('APP_SLUG', 'tenerife_japon_status')
    SITE_ID = 1
    SECRET_KEY = opts.get('SECRET_KEY', 'key')

    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
    LANGUAGE_CODE = 'es'
    TIME_ZONE = 'Europe/Madrid'

    ROOT_URLCONF = 'main.urls'
    WSGI_APPLICATION = 'main.wsgi.application'

    INSTALLED_APPS = [
        # django
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # apps
        'main',
        'toilet',

        # 3rd parties
        'django_extensions',
        'django_yubin',
        'kaio',
        'logentry_admin',
        'channels'
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    # SecurityMiddleware options
    SECURE_BROWSER_XSS_FILTER = True

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                # insert additional TEMPLATE_DIRS here
            ],
            'OPTIONS': {
                'context_processors': [
                    "django.contrib.auth.context_processors.auth",
                    "django.template.context_processors.debug",
                    "django.template.context_processors.i18n",
                    "django.template.context_processors.media",
                    "django.template.context_processors.static",
                    "django.contrib.messages.context_processors.messages",
                    "django.template.context_processors.tz",
                    'django.template.context_processors.request',
                    'constance.context_processors.config',
                ],
                'loaders': [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]
            },
        },
    ]
    if not DEBUG:
        TEMPLATES[0]['OPTIONS']['loaders'] = [
            ('django.template.loaders.cached.Loader', TEMPLATES[0]['OPTIONS']['loaders']),
        ]

    # Bootstrap 3 alerts integration with Django messages
    MESSAGE_TAGS = {
        messages.ERROR: 'danger',
    }

    # Channels
    if DEBUG:
        CHANNEL_LAYERS = {
            "default": {
                "BACKEND": "asgiref.inmemory.ChannelLayer",
                "ROUTING": "toilet.routing.channel_routing",
            },
        }
   else:
        CHANNEL_LAYERS = {
            "default": {
                "BACKEND": "asgi_redis.RedisChannelLayer",
                "CONFIG": {
                    "hosts": [("redis", 6379)],
                },
                "ROUTING": "toilet.routing.channel_routing",
            },
        }
