from DAO.CommandeDAO import CommandeDAO
from DAO.ClientDAO import ClientDAO
from DAO.UserDAO import UserDAO
from entities.Client import Client
from entities.Commande import Commande


user = Commande("sdsd", "2024-10-08", 3 )

usDAO = CommandeDAO() 
print(usDAO.save(user))


# usDAO = ClientDAO() 

# print(usDAO.getOne(3))