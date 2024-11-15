from pydantic import BaseModel


class BookClass(BaseModel):
    topic: str | None
    style: str | None
    language: str | None
    min_pages: str | None
    max_pages: str | None


class TokenData(BaseModel):
    username: str | None = None


class Token(BaseModel):
    access_token: str
    token_type: str