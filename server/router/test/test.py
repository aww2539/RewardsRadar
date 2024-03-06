from flask import Blueprint

test_bp = Blueprint('test_bp', __name__)


@test_bp.route('/test')
def test():
    print("test.py")

    return "<h1>Test Route Successful</h1>"
