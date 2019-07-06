from . import db
from flask_login import UserMixin
from . import login_manager 
from datetime import datetime

class User(UserMixin,db.model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20),index = True)
    email = db.Column(db.String(255),unique = True, index = True)
    bio = db.Column(db.String(1000))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    profile_pic_path = db.Column(db.String)
    password_secure = db.Column(db.String(255))
    blogs = db.relationship('Blog',backref = 'user',lazy = 'dynamic')
    comments = db.relationship('Comment',backref = 'user',lazy = 'dynamic')