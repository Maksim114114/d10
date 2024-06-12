import os
import macdonalc
import celery
from celery import Celery

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'macdonalc.settings')

app = Celery('macdonalc')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()