# Python
from typing import List

# FastAPI
from fastapi import FastAPI, status
from fastapi import Body

# Models
from models import User, UserBase, UserLogin, Tweet

app = FastAPI()

# Path Operations


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
    summary="Shows a single user",
    tags=["Users"]
)
def show_user():
    pass


@app.put(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Updates a single user",
    tags=["Users"]
)
def update_user():
    pass


@app.delete(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Deletes a single user",
    tags=["Users"]
)
def delete_user():
    pass

## Tweets

@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=["Home"],
    summary="Home page"
    )
def home():
    return {"Twitter API": "Running!"}

@app.get(
    path="/tweets",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    tags=["Tweets"],
    summary="Lists tweets"
)
def show_tweets():
    pass

@app.post(
    path="/tweets",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    tags=["Tweets"],
    summary="Posts a new tweet"
)
def post_tweet():
    pass


@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    tags=["Tweets"],
    summary="Shows a single tweet"
)
def show_tweet():
    pass


@app.put(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    tags=["Tweets"],
    summary="Updates a single tweet"
)
def update_tweet():
    pass


@app.delete(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    tags=["Tweets"],
    summary="Deletes a single tweet"
)
def delete_tweet():
    pass