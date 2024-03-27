import uvicorn as uvicorn
from fastapi import FastAPI, Depends, APIRouter,HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, constr, ValidationError, validator, field_validator
from enum import Enum, IntEnum

UserApp = APIRouter()

class User(BaseModel):
    name: constr(pattern=r"^[a-zA-Z0-9_]+$")
    id: int
    age:int

    @field_validator('id')
    def check_age(cls, id):
        if id > 10:
            raise ValueError('error')
        return id

    @field_validator('age')
    def check_age(cls, age):
        if age < 0:
            raise ValueError('error')
        return age

def if_not_1(id: int):
    if id!=1:
        return True
    else:
        return False

AllUser = {}

@UserApp.get("/")
async def get_task():
    return AllUser

@UserApp.get("/{id}")
async def getUser(t_id,if_not_1:bool=Depends(if_not_1)):
    if if_not_1:
        return AllUser[int(t_id)]
    raise HTTPException(status_code=404, detail="oops... you can not get the details")

@UserApp.post("/")
async def add_User(user: User):
    try:
        AllUser[user.id] = user
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return f"Hello {user.name}"


@UserApp.put("/{id}/", response_model=User)
async def update_user(user_id: int, user: User):
    update_item_encoded = jsonable_encoder(user)
    AllUser[user_id] = update_item_encoded
    return update_item_encoded


@UserApp.delete("/{id}/")
async def delete_item(id: int):
    del AllUser[id]
    return {"message": "Item deleted"}
