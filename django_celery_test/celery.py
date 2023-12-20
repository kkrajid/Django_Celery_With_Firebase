
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_test.settings')

app = Celery('django_celery_test')
app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()