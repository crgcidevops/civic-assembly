# -*- coding: utf-8 -*-

# Setup filesystem storage fo static and media
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
THUMBNAIL_DEFAULT_STORAGE = 'django.core.files.storage.FileSystemStorage'
STATIC_ROOT = '/home/.static/'
MEDIA_ROOT = '/home/.media/'

#######   filesystem storage end      #############

EVENTS_ALLOWED_RELATED_MODELS = ['venues', 'organizations']

DEBUG = False
GLOBAL_FOLDERS = ''
