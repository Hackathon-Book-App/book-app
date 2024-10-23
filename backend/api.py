from datetime import timedelta
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm

from pydantic import BaseModel

from BookClass import BookClass
from auth_service import UserAuth
from repository import Users_Test
from recommend_service import recommend_service

ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token(BaseModel):
    access_token: str
    token_type: str

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def health():
    return "I am healthy"


@app.post("/")
def recommend_books(book_properties: Annotated[BookClass, UserAuth.get_current_user]):
    print(book_properties)
    result = recommend_service(book_properties)
    return {'message': result['answer']}


@app.post("/signup")
def sign_in(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user=Users_Test.get_user(form_data.username)
    if not user:
        hashed_password=UserAuth.get_password_hash(form_data.password)
        user = Users_Test(username=form_data.username, hashed_password=hashed_password)
        user.create_users()
        return {'message': 'Signup succesful'}
    return {'message': 'User allready exists, please log in!'}


@app.post("/login")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user: Users_Test = UserAuth.authenticate_user(
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


@app.get("/users/me/", response_model=Users_Test)
async def read_users_me(
    current_user: Annotated[Users_Test, Depends(UserAuth.get_current_active_user)],
):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[Users_Test, Depends(UserAuth.get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]
