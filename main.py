from fastapi import FastAPI
import uvicorn
from database import db_connection
from routes import book_routes


app = FastAPI()

app.include_router(book_routes.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

db_connection.get_connection()
db_connection.create_books_table()
db_connection.create_members_table()
