import os

DEBUG = False
SECRET_KEY = 'topsecret'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] # modified this, because we need to create a new DB once we deploy
# this automatically fetches the value of the URI from the DB Credentials setting when you log into it on Heroku
SQLALCHEMY_TRACK_MODIFICATIONS = False

