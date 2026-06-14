from fastapi import APIRouter, HTTPException
from database.book_db import BooksDB

router = APIRouter()

db_books = BooksDB()


@router.post('/books')
def loc_create_book(data: dict):
    result = db_books.create_book(data)
    return {"message": "Book created successfully", "rows_affected": result}


@router.get('/books')
def loc_get_all_books():
    result = db_books.get_all_books()
    return {"message": "all books displayed successfully", "all_books": result}


@router.get('/books/{id}')
def loc_get_book_by_id(id: int):
    result = db_books.get_book_by_id(id)

    if result is None:
        raise HTTPException(status_code=404, detail="Book not found.")

    return {"message": "one book displayed succssefully", "one_book": result}


@router.patch('/books/{id}')
def loc_update_book(id: int, data: dict):
    result = db_books.update_book(id, data)
    if not result:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book updated successfully"}


'''@router.patch('/books/{id}/borrow/{member_id} ')


@router.patch('/books/{id}/return/{member_id} ')'''
