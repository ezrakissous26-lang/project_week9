from db_connection import get_connection
import mysql.connector

"""CREATE TABLE IF NOT EXISTS books (
        id INT PRIMARY KEY AUTO_INCREMENT,
        title VARCHAR(100) NOT NULL,
        author VARCHAR(50) NOT NULL,
        genre ENUM ('Fiction', 'Non-fiction', 'Science', 'History', 'Other') NOT NULL,
        is_available BOOL DEFAULT TRUE NOT NULL,
        borrow_by_member_id INT
    )
    """


class BooksDB:
    def create_book(self, data: dict):
        conn = get_connection()
        cur = conn.cursor()

        sql_command = "INSERT INTO books (title, author, genre) VALUES (%s, %s, %s)"
        values = list(data.values())
        cur.execute(sql_command, values)
        conn.commit()

        result = cur.rowcount

        cur.close()
        conn.close()

        return result

    def get_all_books(self):
        conn = get_connection()
        cur = conn.cursor(dictionary=True)

        sql_command = "SELECT * FROM books"
        cur.execute(sql_command)

        display = cur.fetchall()

        cur.close()
        conn.close()

        return display

    def get_book_by_id(self, id: int):
        conn = get_connection()
        cur = conn.cursor(dictionary=True)

        sql_command = "SELECT * FROM books WHERE id = %s"
        cur.execute(sql_command, id)

        display = cur.fetchone

        cur.close()
        conn.close()

        return display

    def update_book(self, id: int, data: dict):
        conn = get_connection()
        cur = conn.cursor()

        set_parts = [f"{key} = %s" for key in data.keys()]
        set_clause = " ,".join(set_parts)

        sql_command = f"UPDATE books SET {set_clause} WHERE id = %s"
        values = list(data.values()) + [id]

        cur.execute(sql_command, values)
        conn.commit()

        check = cur.rowcount > 0

        cur.close()
        conn.close()

        return check

    def set_available(self, id: int, val: bool, member_id: int):
        conn = get_connection()
        cur = conn.cursor()

        sql_command = "UPDATE books SET is_available = %s borrow_by_member_id = %s WHERE id = %s"
        values = (val, member_id, id)
        cur.execute(sql_command, values)
        conn.commit()

        check = cur.rowcount > 0

        cur.close()
        conn.close()

        return check

    def count_total_books(self):
        conn = get_connection()
        cur = conn.cursor()

        sql_command = "SELECT COUNT(*) AS total FROM books"
        cur.execute(sql_command)

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result["total"]

    def count_available_books(self):
        conn = get_connection()
        cur = conn.cursor()

        sql_command = "SELECT COUNT(*) AS is_available FROM books WHERE is_available = TRUE"
        cur.execute(sql_command)

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result["is_available"]

    def count_borrowed_books(self):
        conn = get_connection()
        cur = conn.cursor()

        sql_command = "SELECT COUNT(*) AS not_available FROM books WHERE borrow_by_member_id IS NOT NULL"
        cur.execute(sql_command)
        conn.commit()

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result["not_available"]

    def count_by_genre(self, genre: str):
        conn = get_connection()
        cur = conn.cursor()

        sql_command = "SELECT COUNT(*) AS %s FROM books WHERE genre = %s"
        cur.execute(sql_command, genre, genre)

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result[genre]

    def count_active_borrows_by_member(self, member_id):
        conn = get_connection()
        cur = conn.cursor()

        sql_command = "SELECT COUNT(*) AS total_borrow FROM books WHERE borrow_by_member_id = %s"
        cur.execute(sql_command, (member_id,))

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result["total_borrow"]
