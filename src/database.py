from sqlalchemy import inspect
from sqlalchemy.exc import IntegrityError
from .models import (
    KirjaViite,
    ArtikkeliViite,
    KonferenssijulkaisuViite
)

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
    nimi = db.session.query(KirjaViite).all()
    print(nimi)
#Alle teen funktioita jotka sitten sijoittavat tietoa pöytiin.
#Pöydät ovat sittenkin jaoteltu 3 eri pöytään ne löytyvät models.py osiosta.

def create_kirja(key, author, title, year, publisher):
    tarkistus = KirjaViite.query.filter_by(key=key).first()
    if tarkistus :
        print("Key osio ei ole uniikki")
    else:
        viite = KirjaViite(key=key, author=author, title=title, year=year, publisher=publisher)
        db.session.add(viite)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise
        db.session.refresh(viite)
        print(KirjaViite.query.filter_by(key=key).first())

def create_artikkeli(key, author, title, year, journal, volume, pages):
    tarkistus = ArtikkeliViite.query.filter_by(key=key).first()
    if tarkistus :
        print("Key osio ei ole uniikki")
    else:
        viite = ArtikkeliViite(key=key, author=author, title=title,
        year=year, journal=journal, volume=volume, pages=pages)
        db.session.add(viite)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise
        db.session.refresh(viite)
        print(ArtikkeliViite.query.filter_by(key=key).first())

def create_konferenssijulkaisu(key, author, title, year, booktitle):
    tarkistus = KonferenssijulkaisuViite.query.filter_by(key=key).first()
    if tarkistus :
        print("Key osio ei ole uniikki")
    else:
        viite = KonferenssijulkaisuViite(key=key,author=author, title=title, year=year,
        booktitle=booktitle)
        db.session.add(viite)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise
        db.session.refresh(viite)
        print(KonferenssijulkaisuViite.query.filter_by(key=key).first())


def get(key=None, order = "id", descending = True, attribute = "key"):
    #Tehdään apufunktio jolla voi järjestellä ja muokata hakua helpommin.
    def query_avustaja(model):
        q = model.query
        if key:
            if attribute == "key":
                q = q.filter(model.key.ilike(f"%{key}%"))
            elif attribute == "author":
                q = q.filter(model.author.ilike(f"%{key}%"))
            elif attribute == "title":
                q = q.filter(model.title.ilike(f"%{key}%"))
        #Varmistetaan onko arvoa millä pitäisi järjestää haku
        v_order = getattr(model, order, None)
        if v_order is not None:
            if descending:
                q = q.order_by(v_order.desc())
            else:
                q = q.order_by(v_order.asc())
        else:
            #Jos order attribuuttia ei löydy defaultataan id attribuuttiin joka on kaikissa.
            #printataan virhe.
            q = q.order_by(model.id.desc())
            print("order attribuuttia ei löytynyt")
        return q.all()
    #Informaatio tulee takaisin sanakirjana.
    return {
        "kirja": query_avustaja(KirjaViite), 
        "artikkeli": query_avustaja(ArtikkeliViite), 
        "konferenssi": query_avustaja(KonferenssijulkaisuViite)
        }


def delete(key, model):
    if model == "kirja":
        viite=KirjaViite.query.filter_by(key=key).first()
        db.session.delete(viite)
        db.session.commit()
    elif model == "artikkeli":
        viite=ArtikkeliViite.query.filter_by(key=key).first()
        db.session.delete(viite)
        db.session.commit()

    elif model == "konferenssi":
        viite=KonferenssijulkaisuViite.query.filter_by(key=key).first()
        db.session.delete(viite)
        db.session.commit()
def unique_key_check(key):
    #Tarkistetaan onko key uniikki kaikissa pöydissä.
    kirja_tarkistus = KirjaViite.query.filter_by(key=key).first()
    artikkeli_tarkistus = ArtikkeliViite.query.filter_by(key=key).first()
    konferenssi_tarkistus = KonferenssijulkaisuViite.query.filter_by(key=key).first()
    if kirja_tarkistus or artikkeli_tarkistus or konferenssi_tarkistus:
        return False
    return True

def make_entry(entry_type, key, pairs):
    #apufunktio bibtex merkinnän luomiseen
    #Ei lisää tyhjiä kenttiä
    lines = [f"@{entry_type}{{{key},"]
    for name, value in pairs:
        if value:  # None tai tyhjä merkkijono jää pois
            lines.append(f"  {name} = {{{value}}},")
    if lines[-1].endswith(","):
        lines[-1] = lines[-1][:-1]
    lines.append("}")
    return "\n".join(lines) + "\n"

def generate_bibtex():
    #Funktio joka generoi bibtex tiedoston kaikista viitteistä
    entries = []

    for k in KirjaViite.query.all():
        entries.append(make_entry("Book", k.key, [
            ("author", k.author),
            ("title", k.title),
            ("year", k.year),
            ("publisher", k.publisher),
        ]))

    for a in ArtikkeliViite.query.all():
        entries.append(make_entry("Article", a.key, [
            ("author", a.author),
            ("title", a.title),
            ("year", a.year),
            ("journal", a.journal),
            ("volume", a.volume),
            ("pages", a.pages),
        ]))

    for c in KonferenssijulkaisuViite.query.all():
        entries.append(make_entry("Inproceedings", c.key, [
            ("author", c.author),
            ("title", c.title),
            ("year", c.year),
            ("booktitle", c.booktitle),
        ]))

    return "\n".join(entries)