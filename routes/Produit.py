from flask import Blueprint

user_route = Blueprint('produit', __name__)


@user_route.route('/produit')
def hello_world():
    return "<p>Hello, World!</p>"