"""
Django settings for securedrop project.

Generated by 'django-admin startproject' using Django 1.10.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

from __future__ import absolute_import, unicode_literals

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import sys
import logging
logger = logging.getLogger(__name__)

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

DEBUG = False

# Application definition

INSTALLED_APPS = [
    'accounts',
    'blog',
    'cloudflare',
    'common',
    'home',
    'marketing',
    'menus',
    'scanner',
    'search',
    'simple',
    'forms',
    'github',
    'directory',

    'wagtail.contrib.settings',
    'wagtail.contrib.routable_page',
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    # See https://docs.wagtail.io/en/stable/reference/contrib/legacy_richtext.html#legacy-richtext
    'wagtail.contrib.legacy.richtext',
    'wagtail.core',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'wagtailmetadata',
    'wagtailautocomplete',
    'webpack_loader',
    'taggit',
    'rest_framework',
    'wagtailmedia',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.postgres',

    'build',

    'django_logging',

    # Configure the django-otp package.
    'django_otp',
    'django_otp.plugins.otp_totp',
    'django_otp.plugins.otp_static',

    # Enable two-factor auth.
    'allauth_2fa',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

# Must be directly after SecurityMiddleware
if os.environ.get('DJANGO_WHITENOISE'):
    MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')

MIDDLEWARE.extend([
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    'django_logging.middleware.DjangoLoggingMiddleware',

    # Configure the django-otp package. Note this must be after the
    # AuthenticationMiddleware.
    'django_otp.middleware.OTPMiddleware',

    # Reset login flow middleware. If this middleware is included, the login
    # flow is reset if another page is loaded between login and successfully
    # entering two-factor credentials.
    'allauth_2fa.middleware.AllauthTwoFactorMiddleware',

    # Middleware for content security policy
    'csp.middleware.CSPMiddleware',
])


# Django HTTP settings

# Set X-XSS-Protection
SECURE_BROWSER_XSS_FILTER = True

# Set X-Content-Type-Options
SECURE_CONTENT_TYPE_NOSNIFF = True

# We may want to set SECURE_PROXY_SSL_HEADER here


# Make the deployment's onion service name available to templates
ONION_HOSTNAME = os.environ.get('DJANGO_ONION_HOSTNAME')


ROOT_URLCONF = 'securedrop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_settings_export.settings_export',
                'wagtail.contrib.settings.context_processors.settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'securedrop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

if 'DJANGO_DB_HOST' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['DJANGO_DB_NAME'],
            'USER': os.environ['DJANGO_DB_USER'],
            'PASSWORD': os.environ['DJANGO_DB_PASSWORD'],
            'HOST': os.environ['DJANGO_DB_HOST'],
            'PORT': os.environ['DJANGO_DB_PORT'],
            'CONN_MAX_AGE': os.environ.get('DJANGO_DB_MAX_AGE', 600)
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'sdo-build.sqlite3'),
        }
    }


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Search Backend

if 'postgres' in DATABASES['default']['ENGINE']:
    INSTALLED_APPS.append('wagtail.contrib.postgres_search')
    WAGTAILSEARCH_BACKENDS = {
        'default': {
            'BACKEND': 'wagtail.contrib.postgres_search.backend',
        },
    }
else:
    WAGTAILSEARCH_BACKENDS = {}


# Wagtail settings

WAGTAIL_SITE_NAME = "securedrop"

WAGTAILIMAGES_IMAGE_MODEL = 'common.CustomImage'


# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'https://securedrop.org'

# Django-webpack configuration
WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'bundles/',  # must end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'build/static/bundles/webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map']
    }
}

# Disable analytics by default
ANALYTICS_ENABLED = False

# Export analytics settings for use in site templates
SETTINGS_EXPORT = [
    'ANALYTICS_ENABLED',
]
# Prevent template variable name collision with wagtail settings
SETTINGS_EXPORT_VARIABLE_NAME = 'django_settings'

# django-taggit
TAGGIT_CASE_INSENSITIVE = True


# GitHub Webhook Settings

GITHUB_HOOK_SECRET_KEY = os.environ.get(
    'GITHUB_HOOK_SECRET_KEY',
    'default'
).encode('utf-8')

# django-allauth
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)
AUTH_PASSWORD_VALIDATORS = (
    {
        'NAME': 'accounts.password_validation.ZxcvbnValidator',
    },
)

WAGTAIL_FRONTEND_LOGIN_URL = '/accounts/login/'
SITE_ID = 1
LOGIN_REDIRECT_URL = "/"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_UNIQUE_EMAIL = True
SOCIALACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_ADAPTER = 'accounts.users.adapter.MyAccountAdapter'
ACCOUNT_SIGNUP_FORM_CLASS = 'accounts.forms.SignupForm'

# Content Security Policy
# script:
# unsafe-eval for client/common/js/common.js:645 and /client/tor/js/torEntry.js:89
# All for inline scripts in wagtail (admin) login page line 44 and 92
# style:
# #1 through #8needed for inline style for svg in sliding-nav:
# #9 and #10 hashes needed for inline style for modernizr on admin page
# #11 needed for wagtail admin

CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = (
    "'self'",
    "'unsafe-eval'",
    "analytics.freedom.press",
)
CSP_STYLE_SRC = (
    "'self'",
    "'sha256-ZdHxw9eWtnxUb3mk6tBS+gIiVUPE3pGM470keHPDFlE='",
)
CSP_STYLE_SRC_ATTR = (
    "'self'",
    "'unsafe-hashes'",
    "'sha256-ZdHxw9eWtnxUb3mk6tBS+gIiVUPE3pGM470keHPDFlE='",
)
CSP_FRAME_SRC = ("'self'",)
CSP_CONNECT_SRC = (
    "'self'",
    "analytics.freedom.press",
)
CSP_EXCLUDE_URL_PREFIXES = ("/admin", )

# Need to be lists for now so that CSP configuration can add to them.
# This should be reverted after testing.
CSP_IMG_SRC = [
    "'self'",
    "analytics.freedom.press",
]
CSP_OBJECT_SRC = ["'self'"]
CSP_MEDIA_SRC = ["'self'"]

# This will be used to evaluate Google Storage media support in staging
if os.environ.get("DJANGO_CSP_IMG_HOSTS"):
    CSP_IMG_SRC.extend(os.environ["DJANGO_CSP_IMG_HOSTS"].split())
    CSP_MEDIA_SRC.extend(os.environ["DJANGO_CSP_IMG_HOSTS"].split())

# There are also PDF <embeds> in some news posts, so rather than adding to
# default-src, set an explicit object-source
if os.environ.get("DJANGO_CSP_OBJ_HOSTS"):
    CSP_OBJECT_SRC.extend(os.environ["DJANGO_CSP_OBJ_HOSTS"].split())

# Report URI must be a string, not a tuple.
CSP_REPORT_URI = os.environ.get('DJANGO_CSP_REPORT_URI',
                                'https://freedomofpress.report-uri.com/r/d/csp/enforce')


# Logging
#
# Logs are now always JSON. Normally, they go to stdout. To override this for
# development or legacy deploys, set DJANGO_LOG_DIR in the environment.

log_level = os.environ.get("DJANGO_LOG_LEVEL", "info").upper()
log_format = os.environ.get("DJANGO_LOG_FORMAT", "json")
log_stdout = False
log_handler = {
    "formatter": log_format,
    "class": "logging.StreamHandler",
    "stream": sys.stdout,
    "level": log_level,
}

log_dir = os.environ.get("DJANGO_LOG_DIR")
if log_dir:
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_stdout = False
    log_handler = {
        "formatter": log_format,
        "class": "logging.handlers.RotatingFileHandler",
        "filename": os.path.join(log_dir, "django-other.log"),
        "backupCount": 5,
        "maxBytes": 10000000,
        "level": log_level,
    }

DJANGO_LOGGING = {
    "LOG_LEVEL": log_level,
    "CONSOLE_LOG": log_stdout,
    "INDENT_CONSOLE_LOG": 0,
    "DISABLE_EXISTING_LOGGERS": True,
    "PROPOGATE": False,
    "SQL_LOG": False,
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "normal": log_handler,
        "null": {"class": "logging.NullHandler"},
    },
    "formatters": {
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
        },
        "plain": {
            "format": "%(asctime)s %(levelname)s %(name)s "
            "%(module)s %(message)s",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["normal"], "propagate": True,
        },
        "django.template": {
            "handlers": ["normal"], "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["normal"], "propagate": False,
        },
        "django.security": {
            "handlers": ["normal"], "propagate": False,
        },
        # These are already handled by the django json logging library
        "django.request": {
            "handlers": ["null"],
            "propagate": False,
        },
        # Log entries from runserver
        "django.server": {
            "handlers": ["null"], "propagate": False,
        },
        # Catchall
        "": {
            "handlers": ["normal"], "propagate": False,
        },
    },
}
