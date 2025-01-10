import os

class Config:
    # #################################################
    # DB
    # #################################################
    SQLALCHEMY_DATABASE_URI = 'sqlite:///time_tracking.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # #################################################
    # App
    # #################################################
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # #################################################
    # API
    # #################################################
    RESTX_VALIDATE = True