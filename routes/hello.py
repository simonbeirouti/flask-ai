from flask import Blueprint

hello_route_bp = Blueprint('hello', __name__')

@hello_route_bp.route("/hello")
def hello():
    return "Hello, Hooman!!"
