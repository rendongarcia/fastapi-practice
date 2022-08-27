# Python
from uuid import UUID, uuid4
from datetime import date, datetime
from typing import Optional


# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
from pydantic import validator

# Models
class UserBase(BaseModel):    
    user_id: UUID = Field(default_factory=uuid4)
    email: EmailStr = Field(...)


class Password(BaseModel):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
        )


class UserLogin(Password, UserBase):
    pass


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


class UserRegister(Password, User):
    pass


class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ..., 
        min_length=1, 
        max_length=255
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)