from flask import Flask
from routes.User import user_route 
from routes.Client import client_route 
from routes.Commande import commande_route


app = Flask(__name__)
app.secret_key = 'key'

app.register_blueprint(user_route)
app.register_blueprint(client_route)
app.register_blueprint(commande_route)