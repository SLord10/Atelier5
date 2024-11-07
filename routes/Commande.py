from flask import Blueprint, flash, redirect, render_template, request, jsonify, url_for
from datetime import datetime
from DAO.CommandeDAO import CommandeDAO
from DAO.Lign_cmdDAO import Lign_cmdDAO
from DAO.ProduitDAO import ProduitDAO
from DAO.ClientDAO import ClientDAO
from WTF.Commande_WTF import CommandeForm
from entities.Commande import Commande
from entities.Lign_cmd import Ligne_cmd


commande_route = Blueprint('commande_route', __name__)

@commande_route.route('/place_order', methods=['GET', 'POST'])
def place_order():
    form = CommandeForm()
    
    if form.validate_on_submit():
        client_id = form.client_id.data
        product_id = form.product_id.data
        qte = form.qte.data

        # Process the order
        try:
            # Initialize DAOs
            client_dao = ClientDAO()
            produit_dao = ProduitDAO()
            commande_dao = CommandeDAO()
            ligne_cmd_dao = Lign_cmdDAO()
            
            # Fetch the client and product objects
            client = client_dao.getOne(client_id)
            produit = produit_dao.getOne(product_id)
            
            if not client or not produit:
                flash("Client or product not found", "danger")
                return render_template('commande.html', form=form)

            # Create the commande object and save it
            commande = Commande(
                reference="CMD-" + str(datetime.now().timestamp()), 
                date=datetime.now(), 
                client=client
            )
            saved_commande = commande_dao.save(commande)
            
            if not saved_commande:
                flash("Failed to save commande", "danger")
                return render_template('commande.html', form=form)

            # Create and save the ligne_cmd (order line) object
            ligne_cmd = Ligne_cmd(qte=qte, commande=saved_commande, produit=produit)
            ligne_cmd_dao.save(ligne_cmd)

            flash("Order placed successfully", "success")
            return redirect(url_for('commande.place_order'))
        
        except Exception as e:
            print(f"Error placing order: {e}")
            flash(f"An error occurred: {str(e)}", "danger")
            return render_template('commande.html', form=form)
    
    return render_template('commande.html', form=form)