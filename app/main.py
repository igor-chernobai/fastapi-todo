from fastapi import FastAPI

from app.routers.ml import ml_router
from app.routers.tasks import task_router
from app.routers.users import users_router

app = FastAPI()

app.include_router(task_router)
app.include_router(users_router)
app.include_router(ml_router)
