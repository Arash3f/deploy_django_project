from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = '.......'
DEBUG = True

# ------pythonanywhere-------
ALLOWED_HOSTS = ['(account-name).pythonanywhere.com']
# ------pythonanywhere-------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'Portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # ------pythonanywhere-------
        'DIRS': ["/home/(account-name)/(project-name)/templates"],
        # ------pythonanywhere-------
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

WSGI_APPLICATION = 'Portfolio.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # ------pythonanywhere-------
        'NAME': '/home/(account-name)/(project-name)/db.sqlite3',
        # ------pythonanywhere-------
    }
}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

# ------pythonanywhere-------
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    '/home/(account-name)/(project-name)/static',
    '/home/(account-name)/(project-name)/media'
]
STATIC_ROOT = '/home/(account-name)/(project-name)/staticfiles'
MEDIA_ROOT =  '/home/(account-name)/(project-name)/media'
# ------pythonanywhere-------