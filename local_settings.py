# -*- coding: utf-8 -*-

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
THUMBNAIL_DEFAULT_STORAGE = 'django.core.files.storage.FileSystemStorage'


EVENTS_ALLOWED_RELATED_MODELS = ['venues', 'organizations']

STATIC_ROOT = '/home/.static/'
MEDIA_ROOT = '/home/.media/'
DEBUG = False
GLOBAL_FOLDERS = ''
