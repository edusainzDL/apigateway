from fastapi import Query,Path,Body
from app.api.router import api_router as router
from app.api.books.schema import (
    BookCreate,
    BookPath,
    BookResponse,
    BookResponseAll
)
from uuid import UUID
from app.api.books.controller import Controller
@router.get(
    '/books',
    tags = ['Books'],
    response_model = BookResponseAll
)
def get_books():
    return Controller.get_all()

@router.get(
    '/books/{book_id}',
    tags = ['Books'],
    response_model = BookResponse
)
def get_book_id(book_id:UUID = Path(...,description="UUID del libro")):
    return Controller.get_id(book_id)

@router.post(
    '/books',
    tags = ['Books'],
    response_model = BookResponse
)
def create_book(book:BookCreate = Body(...,description="Schema of the book")):
    return Controller.create(book)


@router.patch(
    '/books/{book_id}',
    tags = ['Books'],
    response_model = BookResponse
)
def patch_book(
    book_id:UUID = Path(...,description="UUID del libro"),
    book:BookPath= Body(...,description="Schema of the book")
):
    return Controller.update(book_id,book)

@router.delete(
    '/books/{book_id}',
    tags = ['Books'],
    response_model = BookResponse
)
def delete_book(book_id:UUID = Path(...,description="UUID del libro")):
    return Controller.update(book_id)
