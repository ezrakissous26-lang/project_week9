from fastapi import FastAPI
import uvicorn
from database import db_connection

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

db_connection.get_connection()
db_connection.create_books_table()
db_connection.create_members_table()
