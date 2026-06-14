([GitHub link](https://github.com/ezrakissous26-lang/project_week9))

# PROJECT LIBRARY WEEK9
## Description:
This project is a server-based project that allows the user to manage and manipulate data. This data is contained in a database, which is itself contained within a Docker container. This database has two tables: one for library members and one for books. The activation and invocation of the various functions offered by this program are done via HTTP requests using Postman or the Swagger tool. The project allows the user to retrieve and modify data concerning library members or information about the books.

## Description docker command for sql database:

docker run -d --name libraryproject -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=librarydatabase -p 3306:3306 mysql:8

## Description structure files:
````
───library-api
   │   README.md
   │   requirements.txt
   │
   ├───app
   │   │   main.py
   │   │
   │   └───database
   │           book_db.py
   │           db_connection.py
   │           member_db.py
   │
   ├───logs
   │       app.log
   │
   └───routes
           book_routes.py
           member_routes.py
           report_routes.py
````

## Description structure TABLES:
### members
| שדה | הסבר |
| ----- | ----: |
| `id` | מפתח ראשי |
| `name` | שם החבר, עמודה לא ריקה, מקסימום 50 תווים |
| `email` | כתובת מייל — ייחודית, עמודה לא ריקה |
| `is_active` | האם החבר פעיל — FALSE לא יכול להשאיל עמודה לא ריקה |
| `total_borrows` | מונה סה"כ השאלות — עולה ב-1 בכל השאלה עמודה לא ריקה |
### books
| שדה | הסבר |
| ----- | ----: |
| `id` | מפתח ראשי |
| `title` | כותרת הספר, עמודה לא ריקה, מקסימום 50 תווים |
| `author` | שם המחבר, עמודה לא ריקה, מקסימום 50 תווים |
| `genre` | **ערכי `genre` מותרים:**  Fiction | Non-Fiction | Science | History | Other — מומש כעמודת ENUM במסד הנתונים, כל ערך אחר מחזיר שגיאה, עמודה לא ריקה |
| `is_available` | האם הספר זמין להשאלה — FALSE מסמן הושאל עמודה לא ריקה |
| `borrowed_by_member_id` | מזהה החבר שמחזיק את הספר — NULL אם זמין |

# SYSTEM RULES
## 1. Create book
When the user enters a new book, the system automatically adds `is_available=True` and `borrowed_by=NULL`.
## 2. Genre
Genre only: Fiction / Non-Fiction / Science / History / Other. If the user enter something else the system return `ERROR`
The system need check that also in adding `POST` and updating `PATCH`
## 3. Create member
When the user enters a new member, the system automatically adds `is_available=True` and `total_borrows=0`.
## 4. Email
Need to be unique.
## 5. Member offline
If `is_active=False` you can't borrow book with this user.
## 6. Book not available
If `is_available=False` it's not possible to borrow this book.
## 7. Maximum Books
It's impossible to borrow more than 3 books.
## 8. Return book
It's possible to return book only if this member borrow this book before; logic !

# ENDPOINTS LIST
## Endpoints

### Books

| Method | Endpoint | תיאור |
| :---- | :---- | :---- |
| `POST` | `/books` | יצירת ספר |
| `GET` | `/books` | כל הספרים |
| `GET` | `/books/{id}` | ספר לפי ID |
| `PATCH` | `/books/{id}` | עדכון ספר |
| `PATCH` | `/books/{id}/borrow/{member_id}` | השאלת ספר לחבר |
| `PATCH` | `/books/{id}/return/{member_id}` | החזרת ספר מחבר |

### Members

| Method | Endpoint | תיאור |
| :---- | :---- | ----: |
| `POST` | `/members` | יצירת חבר |
| `GET` | `/members` | כל החברים |
| `GET` | `/members/{id}` | חבר לפי ID |
| `PATCH` | `/members/{id}` | עדכון חבר |
| `PATCH` | `/members/{id}/deactivate` | השבתת חבר |
| `PATCH` | `/members/{id}/activate` | הפעלת חבר |

### Reports

| Method | Endpoint | תיאור |
| :---- | :---- | ----- |
| `GET` | `/reports/summary` | דוח כללי |
| `GET` | `/reports/books-by-genre` | ספרים לפי ז'אנר |
| `GET` | `/reports/top-member` | החבר הכי פעיל |

# WORKFLOW:
http request -> FastAPI routes -> python -> sql-connector python -> DatabseSQL

# Project Architecture

```
Project
│
├── main.py
│   ├── FastAPI
│   ├──  -> create table members()
│   └──  -> create table books()
│
├── database
│   ├── db_connection.py
│   │   └── get_connection()
│   │
│   ├── create table members()
│   └── create table books()
│
├── book_db.py
│   └── class BookDB
│       ├── create_book(data)
│       ├── get_all_books()
│       ├── get_book_by_id(id)
│       ├── update_book(id, data)
│       ├── set_available(id, val, member_id)
│       ├── count_total_books()
│       ├── count_available_books()
│       ├── count_borrowed_books()
│       ├── count_by_genre(genre)
│       └── count_active_borrows_by_members()
│
└── member_db.py
    └── class MemberDB
        ├── create_member(data)
        │
        ├── get_all_members()
        ├── get_member_by_id(id)
        ├── update_member(id, data)
        ├── deactivate_member(id)
        ├── activate_member(id)
        ├── increment_borrows(id)
        ├── count_active_members()
        └── get_top_member()
```

# REGLES D'EXECUTIONS
## 2. Docker installation

`Create container`
- docker run -d --name libraryproject -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=librarydatabase -p 3306:3306 mysql:8

`Execute docker with database`
- docker exec -it libraryproject mysql -uroot -proot -e
## 3. Installation requirements.txt

`pip install -r requirements.txt`
- mysql connector python
- fastapi
- uvicorn