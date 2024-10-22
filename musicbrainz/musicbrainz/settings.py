"""
Django settings for musicbrainz project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "76c1il_*3!n(h6h8i=u%3d^^8gl9m9#$vmm_bkvm1e3q7y$9y)"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "mugio.serveo.net"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.gis",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "entities.apps.EntitiesConfig",  # every django app created needs this
    "social_django",  # social-auth-app-django
    # 'crispy_forms', # django crispy forms
    "leaflet",  # django-leaflet
    "world",  # https://docs.djangoproject.com/en/3.0/ref/contrib/gis/tutorial/
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "musicbrainz.urls"

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
            ]
        },
    }
]

WSGI_APPLICATION = "musicbrainz.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(conn_max_age=600, ssl_require=False)
}
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"


# See https://python-social-auth.readthedocs.io/en/latest/configuration/django.html
# SOCIAL_AUTH_POSTGRES_JSONFIELD = True

AUTHENTICATION_BACKENDS = (
    "social_core.backends.google.GoogleOAuth2",
    "social_core.backends.spotify.SpotifyOAuth2",
    "social_core.backends.musicbrainz.MusicBrainzOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)

SOCIAL_AUTH_STRATEGY = "social_django.strategy.DjangoStrategy"
SOCIAL_AUTH_STORAGE = "social_django.models.DjangoStorage"
# SOCIAL_AUTH_STORAGE = 'app.models.CustomDjangoStorage'

# musicbrainz
SOCIAL_AUTH_MUSICBRAINZ_KEY = os.environ.get("SOCIAL_AUTH_MUSICBRAINZ_KEY", None)
if not SOCIAL_AUTH_MUSICBRAINZ_KEY:
    SOCIAL_AUTH_MUSICBRAINZ_KEY = input("SOCIAL_AUTH_MUSICBRAINZ_KEY:")

SOCIAL_AUTH_MUSICBRAINZ_SECRET = os.environ.get("SOCIAL_AUTH_MUSICBRAINZ_SECRET", None)

# spotify
SOCIAL_AUTH_SPOTIFY_KEY = os.environ.get("SOCIAL_AUTH_SPOTIFY_KEY", None)
if not SOCIAL_AUTH_SPOTIFY_KEY:
    SOCIAL_AUTH_SPOTIFY_KEY = input("SOCIAL_AUTH_SPOTIFY_KEY:")

SOCIAL_AUTH_SPOTIFY_SECRET = os.environ.get("SOCIAL_AUTH_SPOTIFY_SECRET", None)

if not SOCIAL_AUTH_SPOTIFY_SECRET:
    SOCIAL_AUTH_SPOTIFY_SECRET = input("SOCIAL_AUTH_SPOTIFY_SECRET:")

LOGIN_URL = "/entities/login-spotify"
LOGIN_REDIRECT_URL = "/entities"


SOCIAL_AUTH_PIPELINE = (
    "social_core.pipeline.social_auth.social_details",
    "social_core.pipeline.social_auth.social_uid",
    "social_core.pipeline.social_auth.auth_allowed",
    "social_core.pipeline.social_auth.social_user",
    "social_core.pipeline.user.get_username",
    "social_core.pipeline.user.create_user",
    "musicbrainz.pipelines.save_profile",  # <--- set the path to the function
    "social_core.pipeline.social_auth.associate_user",
    "social_core.pipeline.social_auth.load_extra_data",
    "social_core.pipeline.user.user_details",
)


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "null": {
            # Null logger
            "level": "DEBUG",
            "class": "logging.NullHandler",
        },
        "SysLog": {
            # Syslog system logging endpoint, if you want to view messages
            # via mac log viewer etc.
            "level": "DEBUG",
            "formatter": "simple",
            "class": "logging.handlers.SysLogHandler",
            "facility": "local0",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "debug.log",
            "formatter": "verbose",
        },
    },
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)s] %(message)s\n"
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "loggers": {
        "": {
            # Root logger.  All loggers will bubble up to this level
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
        },
        "django.db.backends": {
            # Quieten down the SQL noise, allows us to leave the root
            # logger in DEBUG.
            "handlers": ["null"],  # Quiet by default!
            "propagate": False,
            "level": "WARN",
        },
        "factory": {"handlers": ["console"], "propagate": False, "level": "INFO"},
        "requests": {"handlers": ["console"], "level": "DEBUG", "propagate": True},
        "requests.packages.urllib3.connectionpool": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
        "social_core": {"handlers": ["console"], "level": "DEBUG", "propagate": True},
    },
}
