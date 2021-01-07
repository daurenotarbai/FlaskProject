from . import db
from datetime import datetime
from flask_login import UserMixin

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class CategoryModel(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    category_name = db.Column(db.String(40),nullable=False)
    category_season = db.Column(db.String(100),nullable=False)
    date_created = db.Column(db.DateTime,default = datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id