from DAO.DAO import DAO

class Lign_cmdDAO(DAO):
    def __init__(self) -> None:
        super().__init__()
        self._mycursor = self._myconnection.cursor()

    def save(self, obj) -> None:
        try:
            sql = "INSERT INTO ligne_cmd (qte, commande_id, produit_id) VALUES (%s, %s, %s)"
            val = (obj.qte, obj.commande, obj.produit)
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
            sql = "UPDATE ligne_cmd SET qte = %s, commande_id = %s, produit_id = %s WHERE id = %s"
            val = (obj.quantite, obj.commande.id, obj.produit.id, obj.id)
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
            sql = "DELETE FROM lign_cmd WHERE ligne_cmd_id = %s"
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
            sql = "SELECT * FROM lign_cmd WHERE ligne_cmd_id = %s"
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
            sql = "SELECT * FROM ligne_cmd"
            self._mycursor.execute(sql)
            result = self._mycursor.fetchall()
            return result
        except Exception as e:
            print(f"Error getting records: {e}")
        finally:
            self._mycursor.close()  