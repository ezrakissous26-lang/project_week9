import mysql.connector


def get_connection():
    conn = mysql.connector.connect(
        host="",
        port="",
        user="",
        password="",
        database="",

    )
    print("Successfull connexion !")
    return conn


def create_books_table():
    conn = get_connection()
    cur = conn.cursor()

    sql_command = """
    CREATE TABLE IF NOT EXISTS books (
        id INT PRIMARY KEY AUTO_INCREMENT,
        title VARCHAR(100),
        author VARCHAR(50),
        genre VARCHAR(50),
        is_available BOOL,
        borrow_by_member_id INT
    )
    """
    cur.execute(sql_command)
    conn.commit()

    cur.close()
    conn.close()
    pass


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
    pass
