from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    completed: bool = False


class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool
