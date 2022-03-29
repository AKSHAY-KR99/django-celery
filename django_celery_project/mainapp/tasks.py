from celery import shared_task

@shared_task(bind=True)
def test_function(self):
    # operations
    for i in range(5):
        print(i)
    return "Done"
