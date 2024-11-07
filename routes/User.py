from flask import Blueprint


user_route = Blueprint('user', __name__)


@user_route.route('/user')
def hello_world():
    return "<p>Hello, World!</p>"