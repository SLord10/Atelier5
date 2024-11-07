from DAO.DAO import DAO

class CommandeDAO(DAO):
    def __init__(self) -> None:
        super().__init__()
        self._mycursor = self._myconnection.cursor()

    def save(self, obj) -> int:  
        try:
            sql = "INSERT INTO commande (reference, date, client_id) VALUES (%s, %s, %s)"
            val = (obj.reference, obj.date, obj.client["client_id"])
            self._mycursor.execute(sql, val)
            self._myconnection.commit()
            
            commande_id = self._mycursor.lastrowid
            print("Commande record inserted with ID:", commande_id)
            return commande_id
        except Exception as e:
            print(f"Error inserting record: {e}")
            return None
        finally:
            self._mycursor.close()

    def update(self, obj) -> None:
        try:
            self._mycursor = self._myconnection.cursor()
            sql = "UPDATE commande SET reference = %s, date = %s, client_id = %s WHERE id = %s"
            val = (obj.reference, obj.date, obj.client.id, obj.id)
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
            sql = "DELETE FROM commande WHERE id = %s"
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
            sql = "SELECT * FROM commande WHERE commande_id = %s"
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
            self._mycursor.execute("SELECT * FROM commande")
            result = self._mycursor.fetchall()
            return result
        except Exception as e:
            print(f"Error getting record: {e}")
        finally:
            self._mycursor.close()