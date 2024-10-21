from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from jwt.exceptions import InvalidTokenError
from pydantic import BaseModel
from passlib.context import CryptContext



fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "4c476e40bbc6af8076e4c93e73e350a2c635c83e7d0205b21940c6ab01c9f091"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


class TokenData(BaseModel):
    username: str | None = None


class UserAuth:
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(password):
        return pwd_context.hash(password)

    def get_user(username: str, db=fake_users_db):
        if username in db:
            user_dict = db[username]
            return UserInDB(**user_dict)

    def authenticate_user(username: str, password: str, fake_db=fake_users_db):
        user: UserInDB = UserAuth.get_user(username, fake_db)
        if not user:
            return False
        if not UserAuth.verify_password(password, user.hashed_password):
            return False
        return user

    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_data = TokenData(username=username)
        except InvalidTokenError:
            raise credentials_exception
        user = UserAuth.get_user(
            username=token_data.username, db=fake_users_db)
        if user is None:
            raise credentials_exception
        return user

    async def get_current_active_user(
        current_user: Annotated[User, Depends(get_current_user)],
    ):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user
    
    async def sign_in(form_data: OAuth2PasswordRequestForm):
        hashed_password=UserAuth.get_password_hash(form_data.password)
        #Add to db
        access_token=UserAuth.create_access_token(
            data={"sub":form_data.username},expires_delta=timedelta(minutes=30)
        )
        #TODO Token function or smth, sa nu mai fie in ambele fisiere
        # return Token(access_token,"bearer")
