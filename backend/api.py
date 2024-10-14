from typing import Annotated
from fastapi import Body, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from BookClass import BookClass
from UserCreds import UserCreds
from auth_service import auth
from recommend_service import recommend_service

app = FastAPI()
app.add_middleware(CORSMiddleware,allow_origins=['*'],allow_methods=["*"],allow_headers=["*"] )

@app.post("/")
def recommend_books(book_properties: BookClass):
    print(book_properties)
    result = recommend_service(book_properties)
    return {'message':result[ 'answer']}

@app.post("/auth")
def auth_user(user_creds: UserCreds):
    existing_user=auth(user_creds)  #TODO not implemented
    return existing_user

@app.get("/")
def health():
    return "I am healthy"

