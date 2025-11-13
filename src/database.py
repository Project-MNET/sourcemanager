from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from sqlalchemy.exc import IntegrityError
from . import models
import os

from .init_db import db
#luodaan pöydät tietokantaan.
def luonti():
    db.create_all()
    nimet = list_tables()
    for nimi in nimet:
        print(nimi)

#tarkastetaan onko pöydät luotu.
def list_tables(schema: str = "public") -> list[str]:
    insp = inspect(db.engine)
    return insp.get_table_names(schema=schema)

#Tarkastetaan onko lisätty pöytään:

def hae_tieto():
    nimi = db.session.query(models.Kirja_viite).all()
    print(nimi)
#Alle teen funktioita jotka sitten sijoittavat tietoa pöytiin.
#Pöydät ovat sittenkin jaoteltu 3 eri pöytään ne löytyvät models.py osiosta.

def create_Kirja(author, title, year, publisher):
    viite = models.Kirja_viite(author=author, title=title, year=year, publisher=publisher)
    db.session.add(viite)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise
    db.session.refresh(viite)

def create_artikkeli(author, title, year, journal, volume, pages):
    viite = models.Artikkeli_viite(author=author, title=title, year=year, journal=journal, volume=volume, pages=pages)
    db.session.add(viite)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise
    db.session.refresh(viite)

def create_Konferenssijulkaisu(author, title, year, booktitle):
    viite = models.Konferenssijulkaisu_viite(author=author, title=title, year=year, booktitle=booktitle)
    db.session.add(viite)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise
    db.session.refresh(viite)


