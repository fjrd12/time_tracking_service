from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from src.config import Config

db = SQLAlchemy()
migrate = Migrate()
api = Api(doc='/api_doc/')


def create_app():
    """
    The create_app function wraps the construction of the Flask object, and all
    of the configurations that it needs so that it can later be used to run a local
    server. It also initializes extensions like SQLAlchemy and Marshmallow, as well
    as registering blueprints for API endpoints.

    :return: An instance of the flask application
    :doc-author: Trelent
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    with app.app_context():
        from src.models import User, Task, Category, TimeTrackingRequest
        from src.routes import api_bp, user_ns, category_ns

        app.register_blueprint(api_bp)
        api.add_namespace(user_ns, path='/api/users')
        api.add_namespace(category_ns, path='/api/categories')

        from src.admin import setup_admin
        setup_admin(app)

    return app
