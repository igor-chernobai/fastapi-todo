from celery import Celery

from app.services import fetch_users, save_to_csv

celery_app = Celery('tasks', broker='redis://redis:6379/0')


@celery_app.task
def fetch_users_task():
    users = fetch_users()
    save_to_csv(users)
