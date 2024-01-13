"""
Django settings for crazy_pong project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
# import sys
# print('path:', sys.path)
# print('DB_PORT:', os.getenv('DB_PORT'))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
MEDIA_URL = '/media/'  
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--=!#=6-=b1$xrc=$@7o1s#orkkuskzn+fsx(z&t_4377sisfze'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG') == 'True'

ALLOWED_HOSTS = ['localhost', '*.localhost*', 'crazy-pong.com', '*.crazy-pong.com', '10.11.3.3', '*10.11.3.3']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'game',
    'corsheaders',
    'crazy_pong',
    'channels',
    'accounts',
    'FT_OAuth',
    'twoFA',
    'tournament',
    'authentification',
    'profile',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE')
CSRF_COOKIE_SECURE = os.getenv('CSRF_COOKIE_SECURE')

ROOT_URLCONF = os.getenv('ROOT_URLCONF')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'crazy_pong.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'), 
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'), 
        'PORT': os.getenv('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'


# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost",
    "http://crazy-pong.com",
    "http://10.11.3.3",
]
    # "http://10.11.14.3",

CORS_ALLOW_CREDENTIALS = True
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

##added

ASGI_APPLICATION = 'crazy_pong.asgi.application'


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {"hosts": [("redis", 6379)],},
    },
}

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost",
    "http://crazy-pong.com",
    "https://localhost:8080",
    "http://10.11.3.3",
]
    # "http://10.11.14.3",

CORS_ALLOW_HEADERS = [
    'content-type',
    'language',
]


CORS_ALLOW_ALL_ORIGINS = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'crazypongreal@hotmail.com'
EMAIL_HOST_PASSWORD = '125@conBonus'

# NO VA

# OAUTH2_CLIENT_ID = 'u-s4t2ud-2c2ec0c7f84e7050052f58ecb3b512a3e2182827b1fa480faece0ffed304acc0'
# OAUTH2_CLIENT_SECRET = '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'
# OAUTH2_REDIRECT_URI = 'http://localhost'


# SOCIAL_AUTH_42_KEY = 'u-s4t2ud-2c2ec0c7f84e7050052f58ecb3b512a3e2182827b1fa480faece0ffed304acc0'
# SOCIAL_AUTH_42_SECRET = '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'
# SOCIAL_AUTH_42_SCOPE = ['public', 'profile', 'email']
# SOCIAL_AUTH_42_AUTH_EXTRA_ARGUMENTS = {'response_type': 'code'}

# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'
# LOGIN_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL = '/'


# AUTHENTICATION_BACKENDS = (
#     'social_core.backends.oauth.OAuthAuth',
# )
# NO VA

