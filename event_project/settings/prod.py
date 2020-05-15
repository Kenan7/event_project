from sentry_sdk.integrations.django import DjangoIntegration
import sentry_sdk
from .base import *
from django.core.exceptions import ImproperlyConfigured
import json

DEBUG = False

with open('secrets.json') as f:
    secrets = json.loads(f.read())


sentry_sdk.init(
    dsn=get_secret("SENTRY_URL"),
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)


LOG_LOCATION = BASE_DIR / 'logs' / 'test.log'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': LOG_LOCATION,
        },
    },
    'loggers': {
        'app_user.models': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },

    },
}
