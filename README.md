# FastAPI tweet practice

This is a simple practice project, just for learning FastAPI.

No database supported, it works with dummy JSON files.

Requirements:

- fastapi>=0.68.0,<0.69.0
- pydantic>=1.8.0,<2.0.0
- uvicorn>=0.15.0,<0.16.0
- python-multipart

Usage:

Locate at _app_ folder and run:

~~~
uvicorn main:app --host 0.0.0.0 --port 80 --reload
~~~

Go to `localhost/docs` and try API endpoints.