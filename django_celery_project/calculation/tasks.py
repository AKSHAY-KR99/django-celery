from celery import shared_task

from django_celery_project.celery import app
from .models import Calculations


def fib(n):
    if n < 0:
        raise ValueError("No negative values")
    elif n == 0:
        return 0
    elif n <= 2:
        return 1
    return fib(n - 2) + fib(n - 1)


@shared_task(bind=True)
def fibonacci_task(self, calculation_id):
    calculation = Calculations.objects.get(id=calculation_id)
    try:
        calculation.output = fib(calculation.input)
        calculation.status = Calculations.STATUS_SUCCESS
    except Exception as e:
        calculation.status = Calculations.STATUS_ERROR
        calculation.message = str(e)[:110]
    calculation.save()
    return 'Everything gots well..!!!'
