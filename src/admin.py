from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import User, Task, Category, TimeTrackingRequest
from create_app import db


def setup_admin(app):
    """
    The setup_admin function is used to create the admin interface for the application.
    It takes one argument, app, which is a Flask object. It then creates an Admin object
    and adds views for each of our models.

    :param app: Pass the flask app object to the function
    :return: The admin object
    :doc-author: Trelent
    """
    admin = Admin(app, name='Time Tracking Admin', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Category, db.session))
