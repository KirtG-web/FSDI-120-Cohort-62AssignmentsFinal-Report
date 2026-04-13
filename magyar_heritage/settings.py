"""
Django settings for magyar_heritage project.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-*tn%*9ht*=5-=88m5h03+4fe%of41o=1k2f@nkea1)!j4r070z'

DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # MUST be after SessionMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'magyar_heritage.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]


WSGI_APPLICATION = 'magyar_heritage.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
USE_I18N = True

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('en', 'English'),
    ('hu', 'Hungarian'),
    ('de', 'German'),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

LANGUAGE_COOKIE_NAME = 'django_language'


# Static files
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]


# Email (REAL SMTP CONFIG)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'kirtdgerman13f@gmail.com'
EMAIL_HOST_PASSWORD = 'xxxx xxxx xxxx xxxx'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# If you want to test emails in terminal instead, use this instead:
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'