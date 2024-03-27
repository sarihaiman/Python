import uvicorn as uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, constr, ValidationError, validator, field_validator
from enum import Enum, IntEnum
from TaskRouter import TaskApp
from UserRouter import UserApp
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(TaskApp, prefix='/TaskRouter')
app.include_router(UserApp, prefix='/UserRouter')
app.mount("/Static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=808)