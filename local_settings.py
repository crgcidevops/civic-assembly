# -*- coding: utf-8 -*-

DEBUG = False

EVENTS_ALLOWED_RELATED_MODELS = ['venues', 'organizations']

AWS_STORAGE_BUCKET_NAME = 'civic-local-bucket'
AWS_S3_CUSTOM_DOMAIN = 's3.amazonaws.com'
AWS_S3_SECURE_URLS = False
AWS_S3_PORT = 4569