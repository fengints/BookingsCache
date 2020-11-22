from celery import Celery

app = Celery('BookingsCache')

@app.task()
def mytask():
    print("it is okay")