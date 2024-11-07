from flask import Blueprint, flash, jsonify, render_template
from DAO.CommandeDAO import CommandeDAO
from DAO.Lign_cmdDAO import Lign_cmdDAO
from DAO.ProduitDAO import ProduitDAO

client_route = Blueprint('client', __name__)


@client_route.route('/client/<int:client_id>/commandes', methods=['GET'])
def get_client_commandes(client_id):
    # Instantiate DAO classes
    commande_dao = CommandeDAO()
    lign_cmd_dao = Lign_cmdDAO()
    produit_dao = ProduitDAO()

    try:
        # Retrieve all commandes
        commandes = commande_dao.getAll()
        
        # Filter commandes for the given client_id
        client_commandes = [commande for commande in commandes if commande['client_id'] == client_id]

        # Loop through each commande to fetch associated products and quantities
        for commande in client_commandes:
            # Get all ligne_cmds (line items) for this commande
            ligne_cmds = lign_cmd_dao.getAll()
            produits = []
            
            # Filter ligne_cmds for this specific commande_id
            for ligne_cmd in ligne_cmds:
                if ligne_cmd['commande_id'] == commande['commande_id']:
                    # Get the produit associated with this ligne_cmd
                    produit = produit_dao.getOne(ligne_cmd['produit_id'])  # Assuming you have this method
                    if produit:
                        # Include 'libelle', 'prix', and 'qte' (from ligne_cmd) for each produit
                        produits.append({
                            'libelle': produit['libelle'],
                            'prix': produit['prix'],
                            'qte': ligne_cmd['qte']  # Fetch 'quantite' from ligne_cmd
                        })
            
            # Add the produits list to each commande
            commande['Produits'] = produits

        # Prepare response with data filtered by client_id
        response = {
            "client_id": client_id,
            "commandes": client_commandes
        }

        return jsonify(response), 200  # HTTP status 200 for OK
    
    except Exception as e:
        # In case of an error, log it and return a 500 error
        print(f"Error fetching commandes for client {client_id}: {e}")
        return jsonify({"error": "Unable to fetch commandes"}), 500

