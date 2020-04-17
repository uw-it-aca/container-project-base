from .base_settings import *
import os

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'django_prometheus',
    'django.contrib.humanize',
    'django_user_agents',
    'supporttools',
    'rc_django',
]

TEMPLATES[0]['OPTIONS']['context_processors'].extend([
    'supporttools.context_processors.supportools_globals'
])

if os.getenv('ENV') == 'localdev':
    DEBUG = True
    RESTCLIENTS_DAO_CACHE_CLASS = None
