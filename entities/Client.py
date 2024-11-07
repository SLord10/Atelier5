from entities.User import User
from entities.Commande import Commande


class Client(User):
    def __init__(self,numero, nom, login, password):
        super().__init__(nom, login, password)
        self.__numero = numero
        self.commandes = []
    
    def ajouter_commande(self, commande: Commande):
        self.commandes.append(commande)

    def __repr__(self):
        return f"{self.nom} ({self.__numero})"


