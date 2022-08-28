# Python
import json
from uuid import UUID
from typing import List

# FastAPI
from fastapi import FastAPI, status
from fastapi import Body, Path

# Starlette
from starlette.responses import RedirectResponse

# Models
from models import User, UserBase, UserLogin, Tweet, UserRegister, UserUpdate

# Utils
from utils import append_json_element, search_json_element, search_and_update_json_element, search_and_delete_json_element

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
def sign_up(user: UserRegister = Body(...)):
    """
    Sign Up

    This path operation registers a user in the app
    
    Parameters:

        - Request body parameter
            - user: UserRegister
    
    Returns a JSON with basic user information:
    
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date
    """

    if append_json_element("users.json", user.dict()):
        return user

@app.post(
    path="/auth/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Logins a user",
    tags=["Users"]
)
def login():
    pass


@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Shows all users",
    tags=["Users"]
)
def show_all_users():
    """
    This path operation shows all users in the app

    Parameters:
        - 
    
    Returns a JSON list with all the users in the app, with the following structure:

        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date
    """
    with open("users.json", "r", encoding="utf-8") as f:
        results = json.load(f)
        return results

@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Shows a single user",
    tags=["Users"]
)
def show_user(user_id: UUID = Path(
    ...,
    title="User ID",
    description="User ID"    
    )
):
    """
    This path operation shows a single user

    Parameters:
        - user_id: UUID
    
    Returns a JSON with the user information:

        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date
    """
    user = search_json_element("users.json", "user_id", str(user_id))
    if user:
        return user


@app.put(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Updates a single user",
    tags=["Users"]
)
def update_user(
    user_id: UUID = Path(
        ...,
        title="User ID",
        description="User ID"
    ),
    user: UserUpdate = Body(...)
):
    """
    This path operation updates a single user

    Parameters:
        - user_id: UUID
        - user: UserNoID
    
    Returns a JSON with the user information:

        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date
    """
    new_user = search_and_update_json_element("users.json", "user_id", str(user_id), user.dict())
    if new_user:
        return new_user


@app.delete(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Deletes a single user",
    tags=["Users"]
)
def delete_user(user_id: UUID = Path(
        ...,
        title="User ID",
        description="User ID"
    )
):
    """
    This path operation deletes a single user

    Parameters:
        - user_id: UUID
    
    Returns a JSON with the deleted user information:

        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date
    """
    deleted_user = search_and_delete_json_element("users.json", "user_id", str(user_id))    
    if deleted_user:
        return deleted_user


## Tweets

@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=["Home"],
    summary="Home page"
    )
def home():
    response = RedirectResponse(url="/tweets")
    return response    

@app.get(
    path="/tweets",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    tags=["Tweets"],
    summary="Lists tweets"
)
def show_tweets():
    """
    This path operation shows all tweets in the app

    Parameters:
        - 
    
    Returns a JSON list with all the tweets in the app, with the following structure:

        - tweet_id: UUID 
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
    """
    with open("tweets.json", "r", encoding="utf-8") as f:
        results = json.load(f)
        return results

@app.post(
    path="/tweets",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    tags=["Tweets"],
    summary="Posts a new tweet"
)
def post_tweet(tweet: Tweet = Body(...)):
    """
    Post a tweet

    This path operation posts a new tweet in the app
    
    Parameters:

        - Request body parameter
            - tweet: Tweet
    
    Returns a JSON with basic tweet information:
    
        - tweet_id: UUID 
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
    """

    if append_json_element("tweets.json", tweet.dict()):
        return tweet


@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    tags=["Tweets"],
    summary="Shows a single tweet"
)
def show_tweet(tweet_id: UUID = Path(
    ...,
    title="Tweet ID",
    description="Tweet ID"
)):
    """
    This path operation shows a single tweet

    Parameters:
        - tweet_id: UUID
    
    Returns a JSON with the tweet information:

        - tweet_id: UUID 
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
    """
    tweet = search_json_element("tweets.json", "tweet_id", str(tweet_id))
    if tweet:
        return tweet


@app.put(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    tags=["Tweets"],
    summary="Updates a single tweet"
)
def update_tweet(
    tweet_id: UUID = Path(
        ...,
        title="Tweet ID",
        description="Tweet ID"
    ),
    tweet: Tweet = Body(...)
):
    """
    This path operation updates a single tweet

    Parameters:
        - tweet: Tweet
    
    Returns a JSON with the user information:

        - tweet_id: UUID 
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
    """

    new_tweet = search_and_update_json_element("tweets.json", "tweet_id", str(tweet_id), tweet.dict())
    if new_tweet:
        return new_tweet

@app.delete(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    tags=["Tweets"],
    summary="Deletes a single tweet"
)
def delete_tweet(tweet_id: UUID = Path(
    ...,
    title="Tweet ID",
    description="Tweet ID"
    )
):
    """
    This path operation deletes a single tweet

    Parameters:
        - tweet_id: UUID
    
    Returns a JSON with the deleted tweet information:

        - tweet_id: UUID 
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
    """
    deleted_tweet = search_and_delete_json_element("tweets.json", "tweet_id", str(tweet_id))
    if deleted_tweet:
        return deleted_tweet
