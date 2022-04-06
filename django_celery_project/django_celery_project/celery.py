import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_project.settings')
app = Celery('django_celery_project')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/kolkata')
app.config_from_object(settings, namespace='CELERY')

# # Multiple Workers
# app.conf.task_routers = {
#     'send_mail_app.tasks.send_mail_function': {
#         'queue': 'queue1'
#     },
#     'mainapp.tasks.test_function': {
#         'queue': 'queue2'
#     }
# }

# Celery beat settings
app.conf.beat_schedule = {
    'send_mail_at_our_time': {
        'task': 'send_mail_app.tasks.send_mail_function',  # app_name.file_name.function_name
        'schedule': crontab(hour=18, minute=10),
        # 'args': (2,3) --- the given argument we can use in send_mail_function
    }
}
# app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request : {self.request!r}')
