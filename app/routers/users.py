from fastapi import APIRouter

from app.celery_tasks import fetch_users_task

users_router = APIRouter(prefix='/users', tags=['Users'])


@users_router.post('/import/')
def trigger_fetch_users():
    fetch_users_task.delay()
    return {'message': 'Import started', 'success': True}
