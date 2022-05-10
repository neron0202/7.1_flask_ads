import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1968@localhost/flask"
    SQL_ALCHEMY_TRACK_MODIFICATIONS = False