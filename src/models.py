from flask_sqlalchemy import SQLAlchemy
from .init_db import db

class Kirja_viite(db.Model):
    __tablename__ = "Kirja_viite"
    key = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100))
    title = db.Column(db.String(100))
    year = db.Column(db.Integer)
    publisher = db.Column(db.String(100))

class Artikkeli_viite(db.Model):
    __tablename__ = "Artikkeli_viite"
    key = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100))
    title = db.Column(db.String(100))
    year = db.Column(db.Integer)
    journal = db.Column(db.String(100))
    volume = db.Column(db.Integer)
    pages = db.Column(db.String(100))

class Konferenssijulkaisu_viite(db.Model):
    __tablename__ = "Konferenssijulkaisu_viite"
    key = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100))
    title = db.Column(db.String(100))
    year = db.Column(db.Integer)
    booktitle = db.Column(db.String(100))