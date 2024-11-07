from entities.Commande import Commande


class Produit:
    def __init__(self, libelle, prix):
        self.libelle = libelle
        self.prix = prix
        self.commandes = []
    
    def ajouter_commande(self, commande: Commande ):
        self.commandes.append(commande)

    def __repr__(self) -> str:
        return f"{self.libelle} à {self.prix}$"
    
    def trierProduits(self, lis):
        return sorted(self.commandes, key=lambda commande: commande.date)
    
    def operator_(self, produit):
        return self.prix > produit.prix