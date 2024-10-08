from typing import Annotated
from fastapi import Body, FastAPI

from BookObject import BookClass
from recommend_service import recommend_service


app = FastAPI()


@app.post("/recommend")
def recommend_books(book: BookClass):
    result = recommend_service(book)
    return {'message': result['answer']}
