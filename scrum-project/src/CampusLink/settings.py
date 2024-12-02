import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_URLCONF = 'CampusLink.urls'  # Point this to your 'urls.py' file inside the CampusLink directory

# Debugging mode
DEBUG = True  # Set to False in production

# Allowed hosts
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Database setup
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  # Static files app
    'rest_framework',  # Add DRF to installed apps
    'rest_framework_simplejwt',  # Add SimpleJWT to installed apps
    'apps.accounts',  # Your app
    'apps.posts' ,
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # Use JWT for authentication
    ],
}



# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# Middleware setup
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.staticfiles.middleware.StaticFilesMiddleware',  # Required for serving static files
]

# Firebase Configuration
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate('D:/projectsoft/scrum-project/firebase_config/firebase_admin_sdk.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://campuslink-56ae6-default-rtdb.firebaseio.com'
})

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'

# Directory where static files are collected for deployment
STATICFILES_DIRS = [
    BASE_DIR / "static",  # If you have a 'static' folder in your project directory
]
# Directory where static files are collected for deployment
STATIC_ROOT = BASE_DIR / 'staticfiles'  # This is the directory where 'collectstatic' will place all static files
