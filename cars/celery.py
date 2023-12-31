import os 
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cars.settings')
app = Celery('cars', broker='redis://redis:6379/0', backend='redis://redis:6379/0')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'test': {
        'task': 'telegram.tasks.telegram_mailing',
        'schedule': crontab(0, 0, day_of_month='2')
    }
}