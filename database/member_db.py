from db_connection import get_connection
import mysql.connector


class MembersDB():  # 1
    def create_member(data):
        conn = get_connection()
        cur = conn.cursor()

        sql_command = ""
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        pass

    def get_all_members():  # 2
        conn = get_connection()
        cur = conn.cursor()

        sql_command = ""
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        pass

    def get_member_by_id(id):  # 3
        conn = get_connection()
        cur = conn.cursor()

        sql_command = ""
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        pass

    def update_member(id, data):  # 4
        conn = get_connection()
        cur = conn.cursor()

        sql_command = ""
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        pass

    def activate_member(id):  # 5
        conn = get_connection()
        cur = conn.cursor()

        sql_command = ""
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        pass

    def deactivate_member(id):  # 6
        conn = get_connection()
        cur = conn.cursor()

        sql_command = ""
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        pass

    def increment_borrows(id):  # 7
        conn = get_connection()
        cur = conn.cursor()

        sql_command = ""
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        pass

    def count_active_members():  # 8
        conn = get_connection()
        cur = conn.cursor()

        sql_command = ""
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        pass

    def get_top_member():  # 9
        conn = get_connection()
        cur = conn.cursor()

        sql_command = ""
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        pass
