from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from feedback import tasks

# https://docs.celeryproject.org/en/latest/django/first-steps-with-django.html#django-first-steps
# set the default Django settings module for the celery program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
app = Celery('app')

# Using a string here means the worker will not have to
# pickle the object when using windows
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, tasks.sample_task(), name='add every 10')

    # Calls test('world') every 30 seconds
    # sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    # sender.add_periodic_task(
    #     crontab(hour=7, minute=30, day_of_week=1),
    #     test.s('Happy Mondays!'),
    # )


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
