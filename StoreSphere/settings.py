"""
Django settings for StoreSphere project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from dotenv import load_dotenv
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django_extensions',
    'unfold',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'rest_framework',
    'rest_framework_simplejwt',
    'djoser',
    'store',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'store.middleware.IgnoreFaviconMiddleware',
    'store.middleware.RateLimitMiddleware',
]

ROOT_URLCONF = 'StoreSphere.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'StoreSphere.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

AUTH_USER_MODEL = 'store.User'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

UNFOLD = {
    "SITE_HEADER": _("Store Sphere"),
    "SITE_TITLE": _("Store Sphere"),
    "SITE_SYMBOL": "store",
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "show_recently_visited": True,
        "navigation": [
            {
                "title": _("Users & Groups"),
                "collapsible": True,
                "items": [
                    {
                        "title": _("Users"),
                        "icon": "person",
                        "link": reverse_lazy("admin:store_user_changelist"),
                    },
                    {
                        "title": _("Groups"),
                        "icon": "group",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                ],
            },
            {
                "title": _("Store"),
                "collapsible": True,
                "items": [
                    {
                        "title": _("Products"),
                        "icon": "shopping_cart",
                        "link": reverse_lazy("admin:store_products_changelist"),
                    },
                    {
                        "title": _("Inventorys"),
                        "icon": "inventory",
                        "link": reverse_lazy("admin:store_inventorys_changelist"),
                    },
                    {
                        "title": _("Inventory Products"),
                        "icon": "inventory_2",
                        "link": reverse_lazy("admin:store_inventoryproducts_changelist"),
                    },
                    {
                        "title": _("Stores"),
                        "icon": "store",
                        "link": reverse_lazy("admin:store_stores_changelist"),
                    },
                    {
                        "title": _("Store Products"),
                        "icon": "storefront",
                        "link": reverse_lazy("admin:store_storeproducts_changelist"),
                    },
                    {
                        "title": _("Requests Store To Inventory"),
                        "icon": "request_page",
                        "link": reverse_lazy("admin:store_requestsstoretoinventory_changelist"),
                    },
                    {
                        "title": _("Orders"),
                        "icon": "receipt",
                        "link": reverse_lazy("admin:store_orders_changelist"),
                    },
                    {
                        "title": _("Order Items"),
                        "icon": "list_alt",
                        "link": reverse_lazy("admin:store_orderitems_changelist"),
                    },
                ],
            },
        ],
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

}
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}


AUTH_USER_MODEL = 'store.User'
