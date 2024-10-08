from pydantic import BaseModel


class BookClass(BaseModel):
    topic: str = "any"
    style: str = "any"
    language: str = "any"
    min_pages: str = "0"
    max_pages: str = "2000"