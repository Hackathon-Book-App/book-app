from fastapi import FastAPI
from pydantic import BaseModel

from recommend_service import recommend_service


class Book(BaseModel):
    topic: str = "any"
    style: str = "any"
    language: str = "any"
    min_pages: str = "any"
    max_pages: str = "any"


app = FastAPI()


@app.post("/recommend")
def recommend_books(book: Book):
    result = recommend_service(book)
    return {'message': result['answer']}
