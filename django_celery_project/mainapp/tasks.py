from celery import shared_task


@shared_task(bind=True)
def test_function(self):
    # operations
    for i in range(5):
        print(i)
    return "Done"


@shared_task(bind=True)
def print_akshay(self):
    for i in range(5):
        print(f"AKSHAY-{i + 1}")
    return "Everything set..!!!"
