import os
import sys

path = '/home'
if path not in sys.path:
    sys.path.insert(0, '/home')
path = '/home/cindy'
if path not in sys.path:
    sys.path.insert(0, '/home/cindy')
path = '/home/cindy/myproject'
if path not in sys.path:
    sys.path.insert(0, '/home/cindy/myproject')
path = '/home/cindy/myproject/KHID'
if path not in sys.path:
    sys.path.insert(0, '/home/cindy/myproject/KHID')

os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

