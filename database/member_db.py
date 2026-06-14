from database.db_connection import get_connection
import mysql.connector


class MembersDB():  # 1
    def create_member(self, data):
        conn = get_connection()
        cur = conn.cursor()

        sql_command = "INSERT INTO members (`name`, email) VALUES (%s, %s)"
        values = list(data.values())
        cur.execute(sql_command, values)
        conn.commit()

        last_id = cur.lastrowid

        cur.close()
        conn.close()

        return last_id

    def get_all_members(self):  # 2
        conn = get_connection()
        cur = conn.cursor()

        sql_command = "SELECT * FROM members"
        cur.execute(sql_command)

        result = cur.fetchall()

        cur.close()
        conn.close()

        return result

    def get_member_by_id(self, id):  # 3
        conn = get_connection()
        cur = conn.cursor()

        sql_command = ""
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        pass

    def update_member(self, id, data):  # 4
        conn = get_connection()
        cur = conn.cursor()

        sql_command = ""
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        pass

    def activate_member(self, id):  # 5
        conn = get_connection()
        cur = conn.cursor()

        sql_command = ""
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        pass

    def deactivate_member(self, id):  # 6
        conn = get_connection()
        cur = conn.cursor()

        sql_command = ""
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        pass

    def increment_borrows(self, id):  # 7
        conn = get_connection()
        cur = conn.cursor()

        sql_command = ""
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        pass

    def count_active_members(self):  # 8
        conn = get_connection()
        cur = conn.cursor()

        sql_command = ""
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        pass

    def get_top_member(self):  # 9
        conn = get_connection()
        cur = conn.cursor()

        sql_command = ""
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        pass
