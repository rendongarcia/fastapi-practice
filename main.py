# Python
from typing import List

# FastAPI
from fastapi import FastAPI, status
from fastapi import Body

# Models
from models import User, UserBase, UserLogin

app = FastAPI()

# Path Operations

@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=["Home"])
def home():
    return {"Twitter API": "Running!"}


## Users
@app.post(
    path="/auth/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Registers a new user",
    tags=["Users"]
)
def sign_up():
    pass


@app.post(
    path="/auth/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Logins a user",
    tags=["Users"]
)
def login():
    pass


@app.post(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Shows all users",
    tags=["Users"]
)
def show_all_users():
    pass

@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Shows a user",
    tags=["Users"]
)
def show_user():
    pass

@app.put(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Updates a user",
    tags=["Users"]
)
def update_user():
    pass

@app.delete(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Deletes a new user",
    tags=["Users"]
)
def delete_user():
    pass

## Tweets
