# Python
from uuid import UUID
from datetime import date
from typing import Optional

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
from pydantic import validator

# FastAPI
from fastapi import FastAPI, status
from fastapi import Body

app = FastAPI()


# Models
class UserBase(BaseModel):    
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)


class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8
    )


class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)

    @validator("birth_date")  # Aqui está la magia
    def is_over_eighteen(cls, v):
        todays_date = date.today()
        delta = todays_date - v

        if delta.days/365 <= 18:
            raise ValueError("Must be over 18!")
        else:
            return v


class Tweet(BaseModel):
    pass


@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=["Home"])
def home():
    return {"Twitter API": "Running!"}

