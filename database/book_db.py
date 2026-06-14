from db_connection import get_connection
import mysql.connector


tablebook = """
    CREATE TABLE IF NOT EXISTS books (
        id INT PRIMARY KEY AUTO_INCREMENT,
        title VARCHAR(100),
        author VARCHAR(50),
        genre VARCHAR(50),
        is_available BOOL,
        borrow_by_member_id,
    )
    """


class BooksDB():
    def create_book(data):
        conn = get_connection()
        cur = conn.cursor()

        sql_command = "INSERT INTO books VALUES %s %s %s %s %s"
        cur.execute(sql_command)
        conn.commit()

        check = cur.rowcount()

        cur.close()
        conn.close()

        return check

    def get_all_books():
        conn = get_connection()
        cur = conn.cursor()

        sql_command = "SELECT * FROM books"
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        pass

    def get_book_by_id(id):
        conn = get_connection()
        cur = conn.cursor()

        sql_command = ""
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        pass

    def update_book(id, data):
        conn = get_connection()
        cur = conn.cursor()

        sql_command = ""
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        pass

    def set_available(id, val, member_id):
        conn = get_connection()
        cur = conn.cursor()

        sql_command = ""
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        pass

    def count_total_books():
        conn = get_connection()
        cur = conn.cursor()

        sql_command = ""
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        pass

    def count_available_books():
        conn = get_connection()
        cur = conn.cursor()

        sql_command = ""
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        pass

    def count_borrowed_books():
        conn = get_connection()
        cur = conn.cursor()

        sql_command = ""
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        pass

    def count_by_genre(genre):
        conn = get_connection()
        cur = conn.cursor()

        sql_command = ""
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        pass

    def count_active_borrows_by_member(member_id):
        conn = get_connection()
        cur = conn.cursor()

        sql_command = ""
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        pass
