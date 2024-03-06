from .router import test_bp, home_bp


def create_routes(app):
    app.register_blueprint(test_bp)
    app.register_blueprint(home_bp)
