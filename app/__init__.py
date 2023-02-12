from flask import Flask
from flask_migrate import Migrate
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy


# Globally accessible libraries
from app.database.seeder.FoodDataSeeder import FoodDataSeeder

db = SQLAlchemy()
r = FlaskRedis()


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    r.init_app(app)

    with app.app_context():
        # Include our Routes
        from . import routes

        # Migration
        Migrate(app, db)
        # db.create_all()

        # routes.seed_db()

    return app
