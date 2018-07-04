import os

DEBUG = False
SECRET_KEY = 'topsecret'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] # modified this, because we need to create a new DB once we deploy
SQLALCHEMY_TRACK_MODIFICATIONS = False

