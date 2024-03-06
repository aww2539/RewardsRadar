from flask import Blueprint

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/')
def home():
    print("home.py")

    return "<h1>Homepage Test</h1>"