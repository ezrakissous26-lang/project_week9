from fastapi import APIRouter
from database.book_db import BooksDB

router = APIRouter()

db_books = BooksDB()


@router.post('/books')
def loc_create_book(data: dict):
    result = db_books.create_book(data)
    return {"message": "Book created successfully", "rows_affected": result}


'''@router.get('/books')
def loc_get_all_books():
    db_books.get_all_books()

@router.get('/books/{id}')
def loc_get_book_by_id():
    db_books.get_book_by_id()

@router.patch('/books/{id}')
def loc_update_book():
    db_books.update_book()


@router.patch('/books/{id}/borrow/{member_id} ')


@router.patch('/books/{id}/return/{member_id} ')'''
