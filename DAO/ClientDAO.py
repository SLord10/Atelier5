from DAO.UserDAO import UserDAO

class ClientDAO(UserDAO):
    def __init__(self) -> None:
        super().__init__()

    def save(self, obj) -> None:
        try:
            super().save(obj)
            user_id = self._mycursor.lastrowid  # Get the last inserted user ID

            with self._myconnection.cursor() as cursor:
                sql = "INSERT INTO client (user_id, numero) VALUES (%s, %s)"
                cursor.execute(sql, (user_id, obj._Client__numero))
                self._myconnection.commit()
                print("Client record inserted with user ID:", user_id)
        except Exception as e:
            print(f"Error inserting client record: {e}")

    def update(self, obj) -> None:
        try:
            super().update(obj)

            with self._myconnection.cursor() as cursor:
                sql = "UPDATE client SET numero = %s WHERE user_id = %s"
                val = (obj._Client__numero, obj.id)
                cursor.execute(sql, val)
                self._myconnection.commit()
                print(cursor.rowcount, "client record(s) affected")
        except Exception as e:
            print(f"Error updating client record: {e}")

    def delete(self, obj) -> None:
        try:
            with self._myconnection.cursor() as cursor:
                sql = "DELETE FROM client WHERE user_id = %s"
                cursor.execute(sql, (obj.id,))
                self._myconnection.commit()
                print(cursor.rowcount, "client record(s) deleted")

            super().delete(obj)
        except Exception as e:
            print(f"Error deleting client record: {e}")

    def getOne(self, id: int):
        try:
            with self._myconnection.cursor(dictionary=True) as cursor:
                sql = """
                    SELECT u.*, c.numero, c.client_id
                    FROM user u
                    JOIN client c ON u.user_id = c.user_id
                    WHERE u.user_id = %s
                """
                cursor.execute(sql, (id,))
                return cursor.fetchone()
        except Exception as e:
            print(f"Error getting client record: {e}")

    def getAll(self) -> list:
        try:
            with self._myconnection.cursor(dictionary=True) as cursor:
                sql = """
                    SELECT u.*, c.numero
                    FROM user u
                    JOIN client c ON u.user_id = c.user_id
                """
                cursor.execute(sql)
                return cursor.fetchall()
        except Exception as e:
            print(f"Error getting client records: {e}")
