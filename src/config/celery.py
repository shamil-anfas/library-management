import os
from celery import Celery

# Tell Celery where Django settings are
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Read Celery settings from Django settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Find tasks.py inside apps automatically
app.autodiscover_tasks()
