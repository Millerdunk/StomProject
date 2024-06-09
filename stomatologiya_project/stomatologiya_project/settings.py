"""
Django настройки для проекта mysite.

Сгенерировано с помощью 'django-admin startproject' с использованием Django 3.2.21.

Для получения дополнительной информации по этому файлу, посетите
https://docs.djangoproject.com/en/3.2/topics/settings/

Для полного списка настроек и их значений посетите
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

# Строим пути внутри проекта, используя конструкцию: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Быстрый старт настроек для разработки - не подходит для использования в продакшене
# См. https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# Важно: Секретный ключ должен храниться в секрете в продакшене!
SECRET_KEY = 'django-insecure-@^dh+t-6_(m3zqplitkm)uw5irw5&g+%(537$!4p#%-l+d-96t'

# Важно: Не используйте DEBUG в продакшене!
DEBUG = True

# Список хостов, которые могут обслуживать ваше приложение.
ALLOWED_HOSTS = []


# Определение приложений в проекте
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stomatologiya_app',  # Добавьте свои приложения сюда
]

# Промежуточные слои (middleware) Django
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Определение корневой (root) URL-конфигурации
ROOT_URLCONF = 'stomatologiya_project.urls'

# Определение путей к шаблонам (templates)
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

# Определение пути к файлу WSGI
WSGI_APPLICATION = 'stomatologiya_project.wsgi.application'


# Настройки базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Проверка паролей пользователей
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

AUTH_USER_MODEL = "stomatologiya_app.CustomUser"

# Международные настройки
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Asia/Almaty'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Настройки для статических файлов (CSS, JavaScript, изображения)
STATIC_URL = '/static/' 
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 

# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage' 

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage' 
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# Определение типа первичных ключей для моделей базы данных
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ----------------------------------------для сброса пароля

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 2525
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "millerdunk@mail.ru"
EMAIL_HOST_PASSWORD = "sgd5vmPs8DxpexRjDneF"
EMAIL_FILE_PATH = BASE_DIR / "sent_emails"
DEFAULT_FROM_EMAIL= EMAIL_HOST_USER

LOGIN_REDIRECT_URL = 'adm'