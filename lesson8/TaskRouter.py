import uvicorn as uvicorn
from fastapi import FastAPI, Depends, APIRouter,HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, constr, ValidationError, validator, field_validator
from enum import Enum, IntEnum

TaskApp = APIRouter()

class StatusEnum(str, Enum):
    open = 'open'
    close = 'close'

class Task(BaseModel):
    name: constr(pattern=r"^[a-zA-Z0-9_]+$")
    Des: str
    id: int
    status: StatusEnum


@field_validator('Des')
def check_age(cls, Des):
    if len(Des) > 100:
        raise ValueError('error')
    return Des

    @field_validator('id')
    def check_age(cls, id):
        if id > 10:
            raise ValueError('error')
        return id

AllTask = {}


@TaskApp.get("/")
async def get_task():
    return AllTask


@TaskApp.post("/")
async def add_task(task: Task):
    try:
        AllTask[task.id] = task
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return f"Hello {task.name}"


@TaskApp.put("/{id}/", response_model=Task)
async def update_task(task_id: int, task: Task):
    update_item_encoded = jsonable_encoder(task)
    AllTask[task_id] = update_item_encoded
    return update_item_encoded


@TaskApp.delete("/{id}/")
async def delete_item(id: int):
    del AllTask[id]
    return {"message": "Item deleted"}
