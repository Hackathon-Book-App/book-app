from datetime import timedelta
import shutil
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, UploadFile, status, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import null


from Models import BookClass, Token
from auth_service import UserAuth
from recommend_service import image_service, text_service
from repository import Users_Test

ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=["*"], allow_headers=["*"])


@app.get("/")
def health():
    return "I am healthy"


@app.post("/")
async def recommend_books(request: Request):
    token = request.headers.get('Authorization')
    print(token)
    user: None | Users_Test =UserAuth.get_current_user(token)
    print(user)
    dictul = await request.json()
    book_properties =BookClass
    book_properties.topic=dictul["topic"]
    book_properties.style=dictul["style"]
    book_properties.language=dictul["language"]
    book_properties.min_pages=dictul["min_pages"]
    book_properties.max_pages=dictul["max_pages"]
    if user:
        print(book_properties)
        result = text_service(book_properties)
        return {'message': result['answer']}


@app.post("/image")
def get_image_recommandation(image: UploadFile):

    image_path = "image.jpg"

    with open(image_path, "wb") as f:
        shutil.copyfileobj(image.file, f)

    result = image_service(image_path)

    return {'message': result['answer']}


@app.post("/signup")
def sign_up(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = Users_Test.get_user(form_data.username)
    if not user:
        hashed_password = UserAuth.get_password_hash(form_data.password)
        user = Users_Test(username=form_data.username,
                          hashed_password=hashed_password)
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


@app.post("/getUserBooks")
async def get_user_books(token: Annotated[str, Depends(oauth2_scheme)]):
    return "shut up"