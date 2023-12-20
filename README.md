<h1>Setting up Celery with Django on Windows</h1>

<h2>Introduction</h2>
<p>This guide walks you through the process of setting up Celery with Django on a Windows environment. Celery is a distributed task queue system that can be used to offload time-consuming tasks from your Django application.</p>

<h2>Prerequisites</h2>
<ul>
    <li>Python installed</li>
    <li>Django project set up</li>
    <li>Windows operating system</li>
</ul>

<h2>Step 1: Install Celery</h2>
<pre><code>pip install celery</code></pre>

<h2>Step 2: Create a Django App</h2>
<pre><code>django-admin startapp mainapp</code></pre>

<h2>Step 3: Install Redis on Windows</h2>
<p>Follow the instructions at <a href="https://github.com/tporadowski/redis/releases" target="_blank">https://github.com/tporadowski/redis/releases</a>.</p>
<p>After installation, open a command prompt, navigate to C:\Program Files\Redis\, and run:</p>
<pre><code>redis-cli.exe</code></pre>
<p>Verify if Redis is running:</p>
<pre><code>127.0.0.1:6379&gt; ping
PONG
127.0.0.1:6379&gt;</code></pre>

<h2>Step 4: Configure Celery Settings</h2>
<pre><code># settings.py

CELERY_BROKER_URL = "redis://127.0.0.1:6379"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'</code></pre>

<h2>Step 5: Create Celery Configuration</h2>
<pre><code># celery.py

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
    print(f"Request: {self.request!r}")</code></pre>

<h2>Step 6: Create a Celery Task</h2>
<pre><code># mainapp/tasks.py

from celery import shared_task

@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return "Done"</code></pre>

<h2>Step 7: Update Your Views</h2>
<pre><code># mainapp/views.py

from django.shortcuts import render, HttpResponse
from .tasks import test_func

def test(request):
    test_func.delay()
    return HttpResponse("Done")</code></pre>

<h2>Step 8: Install Redis Python Package</h2>
<pre><code>pip install redis</code></pre>

<h2>Step 9: Run Celery Worker</h2>
<pre><code>celery -A your_project_name.celery worker -l info</code></pre>
<p>For Windows:</p>
<pre><code>celery -A your_project_name.celery worker --pool=solo -l info</code></pre>

<h2>Step 10: Update Django Settings</h2>
<pre><code># settings.py

CELERY_RESULT_BACKEND = "django-db"</code></pre>
<p>Install Django Celery Results:</p>
<pre><code>pip install django-celery-results</code></pre>

<h2>Step 11: Update __init__.py in Project Folder</h2>
<pre><code># __init__.py

from .celery import app as celery_app

__all__ = ('celery_app',)</code></pre>

<h2>Step 12: Install Django Celery Beat</h2>
<pre><code>pip install django-celery-beat</code></pre>

<h2>Step 13: Run Celery Beat</h2>
<pre><code>celery -A your_project_name beat -l info</code></pre>

<p>This guide assumes a basic understanding of Django and Celery. If you encounter any issues, refer to the official documentation for more details: Django | Celery.</p>
