from pydantic import BaseModel


class BookClass(BaseModel):
    topic: str 
    style: str 
    language: str 
    min_pages: str 
    max_pages: str 