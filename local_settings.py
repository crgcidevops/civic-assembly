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

if 'test' not in sys.argv:
	mtc_applications = [
	    'venues_bike_share_station',
	    'venues_traffic_camera',
	    'venues_hov_lane',
	    'venues_toll_point',
	    'venues_traffic_sign',
	    'venues_transit_stop'
	]


	from django.conf import settings

	print len(settings.INSTALLED_APPS)

	for mtc_app in [app for app in mtc_applications if app in settings.INSTALLED_APPS]:
		settings.INSTALLED_APPS.remove(mtc_app)

	print "\n", "*"*50, "\nMTC applications was deleted from INSTALL_APPS\n", "*"*50, "\n"
	print len(settings.INSTALLED_APPS)
