import os
from pathlib import Path

import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
# for best-practices.

# SECURITY WARNING: keep the secret key used in production secret!
# Please set SECRET_KEY environment variable in your production environment
# (e.g. Heroku).
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-%rxz&0@$vek)e7-%o!1dhwm^j-xz*c#574p=7-sxl241%&ora*')

# Automatically determine environment by detecting if DATABASE_URL variable.
# DATABASE_URL is provided by Heroku if a database add-on is added
# (e.g. Heroku Postgres).
PRODUCTION = os.getenv('DATABASE_URL') is not None

# SECURITY WARNING: don't run with debug turned on in production!
# If you want to enable debugging on Heroku for learning purposes,
# set this to True.
DEBUG = not PRODUCTION

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME', '')

ALLOWED_HOSTS = [f'{HEROKU_APP_NAME}.herokuapp.com']

if not PRODUCTION:
    ALLOWED_HOSTS += ['.localhost', '127.0.0.1', '[::1]']


# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'main',
    'barang',
    'chat',
    'channels',
    'keranjang',
    'transaksi',
    'admin_warung',
    'review',
    'visualisasi_data',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'warung_etik.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
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
]

WSGI_APPLICATION = 'warung_etik.wsgi.application'
ASGI_APPLICATION = "warung_etik.asgi.application"

# Channels for chat, TODO change param for deployment.
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'TEST': {
            'NAME': os.path.join(BASE_DIR, 'db_test.sqlite3')
        }
    }
}

# Set database settings automatically using DATABASE_URL.
if PRODUCTION:
    DATABASES['default'] = dj_database_url.config(
        conn_max_age=600, ssl_require=True
    )


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/
# Feel free to change these according to your needs.

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': []
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# This is the directory for storing `collectstatic` results.
# This shouldn't be included in your Git repository.
STATIC_ROOT = BASE_DIR / 'staticfiles'

# You can use this directory to store project-wide static files.
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Make sure the directories exist to prevent errors when doing `collectstatic`.
for directory in [*STATICFILES_DIRS, STATIC_ROOT]:
    directory.mkdir(exist_ok=True)

# Enable compression and caching features of whitenoise.
# You can remove this if it causes problems on your setup.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
