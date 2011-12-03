from settings import CACHES

DEBUG = True
SERVE_MEDIA = DEBUG
TEMPLATE_DEBUG = DEBUG
EMAIL_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG

CACHES['default']['BACKEND'] = 'django.core.cache.backends.dummy.DummyCache'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

