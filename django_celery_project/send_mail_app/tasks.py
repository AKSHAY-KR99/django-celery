from django_celery_project import settings
from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail


@shared_task(bind=True)
def send_mail_function(self):
    users = get_user_model().objects.all()
    for user in users:
        subject = "Celery Testing"
        message = "Testing the email scheduling using celery"
        to_mail = user.email
        print(to_mail)
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_mail],
            fail_silently=True
        )
    return "Done"
