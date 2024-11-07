class Commande:
    def __init__(self, reference, date, client):
        self.reference = reference
        self.date = date
        self.client= client
        self.produits = []
    
    def ajouter_produit(self, produit):
        self.produits.append(produit)


    def __repr__(self):
        return str(self)