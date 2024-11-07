from abc import ABC, abstractmethod
import mysql.connector
from mysql.connector import Error

# Dao Pattern abstract class
class DAO(ABC):

    def __init__(self) -> None:
        super().__init__()
        try:
            # Protected to manage the connection with the database
            self._myconnection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="Atelier5"
            )
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            self._myconnection = None

    @abstractmethod
    def save(self, obj) -> None:
        pass

    @abstractmethod
    def update(self, obj) -> None:
        pass

    @abstractmethod
    def delete(self, obj) -> None:
        pass

    @abstractmethod
    def getOne(self, id: int):
        pass

    @abstractmethod
    def getAll(self) -> list:
        pass
