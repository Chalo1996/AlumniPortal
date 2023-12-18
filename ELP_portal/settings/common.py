"""
Django settings for ELP_portal project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from datetime import timedelta
from typing import List

import cloudinary.uploader
import django_heroku
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

ALLOWED_HOSTS: List[str] = []

# Application definition
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_LIBRARIES = [
    # third party libraries
    # "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "corsheaders",
    "drf_yasg",
    # 'widget_tweaks',
]

LOCAL_APPS = [
    # apps
    "app.user_module",
    "app.authentication",
    "app.events",
    "app.hubs",
    "app.alumni",
    "app.chapters",
    "app.opportunities",
    "app.feedback",
    "app.news",
    "app.analytics",
    "app.profile",
    "app.posts",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_LIBRARIES + LOCAL_APPS


# CORS settings
CORS_ALLOWED_ORIGINS: List[str] = []
# CORS_ALLOWED_ORIGINS_REGEXES: List[str] = []
# CORS_URLS_REGEX = r"^/api/.*$"

# CSRF_TRUSTED_ORIGINS = ["https://aspiring-treatment-production.up.railway.app/"]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.MultiPartParser",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 1000,
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=14),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}

AUTH_USER_MODEL = "user_module.User"

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"}
    }
}

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

ROOT_URLCONF = "ELP_portal.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ELP_portal.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        "OPTIONS": {"user_attributes": ["email", "username"]},
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 8},
    },
]

# Caching Using django_redis
# https://django-redis.readthedocs.io/en/latest/

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.HerdClient",
            "PICKLE_VERSION": -1,
            "SOCKET_CONNECT_TIMEOUT": 10,
            "SOCKET_TIMEOUT": 10,
        },
        "KEY_PREFIX": "elpportal_cache"
    }
}

# Use cache for session storage
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# Set TTL for cache
# Set to 1 day

CACHE_TTL = 60 * 30

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Nairobi"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

# configuring the location for media
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Configure Django App for Heroku.
django_heroku.settings(locals())
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

cloudinary.config(
    cloud_name=config("CLOUDINARY_CLOUD_NAME", ""),
    api_key=config("CLOUDINARY_API_KEY", ""),
    api_secret=config("CLOUDINARY_API_SECRET", ""),
    secure=True,
)

# Mail server
EMAIL_HOST = (
    os.environ["EMAIL_HOST"]
    if "EMAIL_HOST" in os.environ
    else config("EMAIL_HOST")
)
EMAIL_PORT = (
    os.environ["EMAIL_PORT"]
    if "EMAIL_PORT" in os.environ
    else config("EMAIL_PORT")
)
EMAIL_HOST_USER = (
    os.environ["EMAIL_HOST_USER"]
    if "EMAIL_HOST_USER" in os.environ
    else config("EMAIL_HOST_USER")
)
EMAIL_HOST_PASSWORD = (
    os.environ["EMAIL_HOST_PASSWORD"]
    if "EMAIL_HOST_PASSWORD" in os.environ
    else config("EMAIL_HOST_PASSWORD")
)
EMAIL_USE_SSL = (
    os.environ["EMAIL_USE_SSL"]
    if "EMAIL_USE_SSL" in os.environ
    else config("EMAIL_USE_SSL")
)
DEFAULT_FROM_EMAIL = (
    os.environ["DEFAULT_FROM_EMAIL"]
    if "DEFAULT_FROM_EMAIL" in os.environ
    else config("DEFAULT_FROM_EMAIL")
)


# SMS Gateway
SMS_GATEWAY_API_KEY = (
    os.environ["SMS_GATEWAY_API_KEY"]
    if "SMS_GATEWAY_API_KEY" in os.environ
    else config("SMS_GATEWAY_API_KEY")
)
SMS_SENDER_ID = (
    os.environ["SMS_SENDER_ID"]
    if "SMS_SENDER_ID" in os.environ
    else config("SMS_SENDER_ID")
)
