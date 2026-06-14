import mysql.connector


def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="1234",
        database="librarydatabase",

    )
    print("Successfull connexion !")
    return conn


def create_books_table():
    conn = get_connection()
    cur = conn.cursor()

    sql_command = """CREATE TABLE IF NOT EXISTS books (
        id INT PRIMARY KEY AUTO_INCREMENT,
        title VARCHAR(100) NOT NULL,
        author VARCHAR(50) NOT NULL,
        genre ENUM ('Fiction', 'Non-fiction', 'Science', 'History', 'Other') NOT NULL,
        is_available BOOL DEFAULT TRUE NOT NULL,
        borrowed_by_member_id INT
    )
    """

    cur.execute(sql_command)
    conn.commit()

    cur.close()
    conn.close()


def create_members_table():
    conn = get_connection()
    cur = conn.cursor()

    sql_command = """
    CREATE TABLE IF NOT EXISTS members (
        id INT PRIMARY KEY AUTO_INCREMENT,
        email VARCHAR(100),
        name VARCHAR(50),
        is_active BOOL,
        total_borrows INT
    )
    """
    cur.execute(sql_command)
    conn.commit()

    cur.close()
    conn.close()
