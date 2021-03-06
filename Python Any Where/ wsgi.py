# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

# assuming your django settings file is at '/home/Arash3f/mysite/mysite/settings.py'
# and your manage.py is is at '/home/Arash3f/mysite/manage.py'
path = '/home/(Account-name)/(project-name)'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = '(app-name).settings'

# then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()