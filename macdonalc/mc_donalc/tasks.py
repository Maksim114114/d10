from celery import shared_task
import time
import redis



@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")



@shared_task
def printer(N):
    for i in range(N):
        time.sleep(1)
        print(i+1)
