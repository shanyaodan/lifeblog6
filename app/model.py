# --*-- coding: utf-8 --*--
from . import db


class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	users = db.relationship('User', backref='roles')


class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	realname = db.Column(db.String(64));
	nickname = db.Column(db.String(64));
	role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))