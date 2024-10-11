from typing import Annotated
from fastapi import Body, FastAPI

from BookClass import BookClass
from UserCreds import UserCreds
from auth_service import auth
from recommend_service import recommend_service

app = FastAPI()


@app.post("localhost:8000")
def recommend_books(book: Annotated[BookClass, Body(embed=True)]):
    result = recommend_service(book)
    return {'message': result['answer']}

@app.post("/auth")
def auth_user(user_creds: UserCreds):
    existing_user=auth(user_creds)  #TODO not implemented
    return existing_user