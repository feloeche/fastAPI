#Python
from uuid import UUID
from datetime import date
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI
from pydantic.networks import EmailStr
from pydantic import Field


app = FastAPI()

# Models

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
        password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        )
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        )
    birth_date: Optional[date] = Field(default=None)

class TWeet(BaseModel):
    pass

@app.get(path="/")
def home():
    return {"Twitter API": "Working"}