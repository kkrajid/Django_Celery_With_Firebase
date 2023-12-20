Setting up Celery with Django on Windows
Install Celery
bash
Copy code
pip install celery
Create a Django App
bash
Copy code
django-admin startapp mainapp
Install Redis on Windows
Follow the instructions at https://github.com/tporadowski/redis/releases.

After installation, navigate to C:\Program Files\Redis\ and run:

bash
Copy code
redis-cli.exe
Then, check if Redis is running:

bash
Copy code
127.0.0.1:6379> ping
PONG
127.0.0.1:6379>
Celery Settings
In your Django project's settings, add the following:

python
Copy code
# celery settings

CELERY_BROKER_URL = "redis://127.0.0.1:6379"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'
Create Celery Configuration
Create celery.py in your project folder:

python
Copy code
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
app = Celery('your_project_name')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')
app.config_from_object(settings, namespace='CELERY')

# Celery Beat settings
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
Create Celery Task
Create tasks.py in your app:

python
Copy code
from celery import shared_task

@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return "Done"
Update Your Views
In your views.py, add:

python
Copy code
from django.shortcuts import render, HttpResponse
from .tasks import test_func

def test(request):
    test_func.delay()
    return HttpResponse("Done")
Install Redis Python Package
bash
Copy code
pip install redis
Run Celery Worker
bash
Copy code
celery -A your_project_name.celery worker -l info
For Windows:

bash
Copy code
celery -A your_project_name.celery worker --pool=solo -l info
Update Django Settings
Add the following to your Django settings:

python
Copy code
CELERY_RESULT_BACKEND = "django-db"
Install Django Celery Results:

bash
Copy code
pip install django-celery-results
Update __init__.py in Project Folder
Add the following to __init__.py in your project folder:

python
Copy code
from .celery import app as celery_app

__all__ = ('celery_app',)
Install Django Celery Beat
bash
Copy code
pip install django-celery-beat
Run Celery Beat
bash
Copy code
celery -A your_project_name beat -l info
This guide assumes a basic understanding of Django and Celery. If you encounter any issues, refer to the official documentation for more details: Django | Celery.






