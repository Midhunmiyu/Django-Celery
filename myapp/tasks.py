from celery import shared_task
from time import sleep

@shared_task
def sub(x,y):
    sleep(5)
    return x - y

@shared_task
def clear_session_cache(id):
    print(f'session cleared of id {id}')
    return id