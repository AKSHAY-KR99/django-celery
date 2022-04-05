import json

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_function
from send_mail_app.tasks import send_mail_function
from django_celery_project import settings
from django_celery_beat.models import PeriodicTask, CrontabSchedule


def test(request):
    test_function.delay()
    return HttpResponse("Done")


def send_mail_to_all(request):
    send_mail_function.delay()
    return HttpResponse("Emails sends")


def send_email_testing(request):
    try:
        send_mail(
            subject="AKSHAY",
            message="Testing the mail sending functin is working or not.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['akshayakr4@gmail.com'],
            fail_silently=True
        )
    except Exception as e:
        print(e)
    return HttpResponse("Function works well")


def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=15, minute=2)
    tasks = PeriodicTask.objects.create(crontab=schedule, task='send_mail_app.tasks.send_mail_function',
                                        name=f'schedule_mail_task_{3}')
    return HttpResponse("!..Sent..!")


def get_periodic_tasks(request):
    tasks = PeriodicTask.objects.all()
    for task in tasks:
        print(task)
    return HttpResponse("Thank you..")
