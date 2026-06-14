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

        sql_command = "SELECT * FROM members WHERE id = %s"
        cur.execute(sql_command, (id,))

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result

    def update_member(self, id: int, data: dict):  # 4
        conn = get_connection()
        cur = conn.cursor()

        set_parts = [f"{key} = %s" for key in data.keys()]
        set_clause = ", ".join(set_parts)

        sql_command = f"UPDATE members SET {set_clause} WHERE id = %s"
        values = list(data.values()) + [id]
        cur.execute(sql_command, values)
        conn.commit()

        check = cur.rowcount > 0

        cur.close()
        conn.close()

        return check

    def activate_member(self, id):  # 5
        conn = get_connection()
        cur = conn.cursor()

        sql_command = "UPDATE members SET is_active = TRUE WHERE id = %s"
        cur.execute(sql_command, (id,))
        conn.commit()

        check = cur.rowcount > 0

        cur.close()
        conn.close()

        return check

    def deactivate_member(self, id):  # 6
        conn = get_connection()
        cur = conn.cursor()

        sql_command = "UPDATE members SET is_active = FALSE WHERE id = %s"
        cur.execute(sql_command, (id,))
        conn.commit()

        check = cur.rowcount > 0

        cur.close()
        conn.close()

        return check


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
