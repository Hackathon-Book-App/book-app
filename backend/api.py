from datetime import timedelta
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from BookClass import BookClass
from User import User, UserAuth, UserInDB
from recommend_service import recommend_service

ACCESS_TOKEN_EXPIRE_MINUTES = 1

app = FastAPI()

class Token(BaseModel):
    access_token: str
    token_type: str

app.add_middleware(CORSMiddleware, allow_origins=[
                   '*'], allow_methods=["*"], allow_headers=["*"])


@app.post("/")
def recommend_books(book_properties: BookClass):
    print(book_properties)
    result = recommend_service(book_properties)
    return {'message': result['answer']}


@app.get("/")
def health():
    return "I am healthy"


@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user: UserInDB = UserAuth.authenticate_user(
        form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = UserAuth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@app.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(UserAuth.get_current_active_user)],
):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(UserAuth.get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]
