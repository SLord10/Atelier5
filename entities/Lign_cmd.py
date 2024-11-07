from entities.Commande import Commande
from entities.Produit import Produit


class Ligne_cmd:
    def __init__(self, qte, produit , commande):
        self.qte = qte
        self.produit = produit
        self.commande = commande
    
    def __repr__(self) -> str:
        return f"{self.qte} {self.produit} pour {self.commande}"