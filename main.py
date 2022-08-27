# Python
import json
from typing import List

# FastAPI
from fastapi import FastAPI, status
from fastapi import Body

# Models
from models import User, UserBase, UserLogin, Tweet, UserRegister

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

    with open("users.json", "r+", encoding="utf-8") as f:
        results = json.load(f)
                
        user_dict = user.dict()
        results.append(user_dict)

        f.seek(0)
        json.dump(results, f, default=str, indent=4)
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

    with open("tweets.json", "r+", encoding="utf-8") as f:
        results = json.load(f)
                
        tweet_dict = tweet.dict()
        results.append(tweet_dict)

        f.seek(0)
        json.dump(results, f, default=str, indent=4)
        return tweet


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