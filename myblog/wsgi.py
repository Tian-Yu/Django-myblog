"""
WSGI config for myblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")
from os.path import join,dirname,abspath

PROJECT_DIR = dirname(dirname(abspath(__file__)))
import sys 
sys.path.insert(0,PROJECT_DIR) 

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()