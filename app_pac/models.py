from datetime import datetime
from app_pac import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(250), index=True)
    password = db.Column(db.String(100), index=True)
    advert = db.relationship('adverts', backref='author', lazy='dynamic')

    def __init__(self, login, password, advert):
        self.login = login
        self.password = password
        self.advert = advert

    def _repr__(self):
        return f''

class Advert(db.Model):
    __tablename__ = 'adverts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True)
    description = db.Column(db.String(240), index=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))   #, db.ForeignKey('users.id')

    def __init__(self, title, description, created_at, user_id):
        self.title = title
        self.description = description
        self.created_at = created_at
        self.user_id = user_id

    def _repr__(self):
        return f''
