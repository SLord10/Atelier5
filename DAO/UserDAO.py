from DAO.DAO import DAO

class UserDAO(DAO):
    def __init__(self) -> None:
        super().__init__()
        self._mycursor = self._myconnection.cursor()

    def save(self, obj) -> None:
        try:
            sql = "INSERT INTO user (nom,login, password) VALUES (%s, %s, %s)"
            val = (obj._nom, obj._login, obj._password)
            self._mycursor.execute(sql, val)
            self._myconnection.commit()
            print(self._mycursor.rowcount, "record inserted.")
        except Exception as e:
            print(f"Error inserting record: {e}")
        finally:
            self._mycursor.close()

    def update(self, obj) -> None:  
        try:
            self._mycursor = self._myconnection.cursor()
            sql = "UPDATE user SET nom = %s, login = %s, password = %s WHERE id = %s"
            val = (obj.nom, obj.login, obj.password,  obj.id)
            self._mycursor.execute(sql, val)
            self._myconnection.commit()
            print(self._mycursor.rowcount, "record(s) affected")
        except Exception as e:
            print(f"Error updating record: {e}")
        finally:
            self._mycursor.close()

    def delete(self, obj) -> None:  
        try:
            self._mycursor = self._myconnection.cursor()
            sql = "DELETE FROM user WHERE id = %s"
            val = (obj.id,)
            self._mycursor.execute(sql, val)
            self._myconnection.commit()
            print(self._mycursor.rowcount, "record(s) deleted")
        except Exception as e:
            print(f"Error deleting record: {e}")
        finally:
            self._mycursor.close()

    def getOne(self, id: int):  
        try:
            self._mycursor = self._myconnection.cursor(dictionary=True)
            sql = "SELECT * FROM user WHERE user_id = %s"
            val = (id,)
            self._mycursor.execute(sql, val)
            result = self._mycursor.fetchone()
            return result
        except Exception as e:
            print(f"Error getting record: {e}")
        finally:
            self._mycursor.close()

    def getAll(self) -> list:
        try:
            self._mycursor = self._myconnection.cursor(dictionary=True)
            sql = "SELECT * FROM user"
            self._mycursor.execute(sql)
            result = self._mycursor.fetchall()
            return result
        except Exception as e:
            print(f"Error getting records: {e}")
        finally:
            self._mycursor.close()
            