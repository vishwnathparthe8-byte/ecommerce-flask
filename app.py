from flask import Flask, render_template
from config import Config
from models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # -------- Home / Landing Page for Role Selection -------- #
    @app.route("/")
    def home():
        return render_template("users/choose_role.html")  # Role selection page

    # Import blueprints
    from routes.users import users_bp
    from routes.products import products_bp
    from routes.orders import orders_bp

    # Register blueprints
    app.register_blueprint(users_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(orders_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
    