from pydantic import BaseModel


class BookClass(BaseModel):
    topic: str 
    style: str 
    language: str 
    min_pages: str 
    max_pages: str 


class TokenData(BaseModel):
    username: str | None = None


class Token(BaseModel):
    access_token: str
    token_type: str