import sys, os
sys.path.append(os.path.abspath("."))

from flask import Flask, redirect, render_template
from flask_wtf import CSRFProtect
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from forms import ReferenceForm
from database import create_artikkeli, create_Kirja, create_Konferenssijulkaisu

from init_db import db, init
from src import database, models
load_dotenv()

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)
init(app) #tämä yhdistää dbn flask applikaatioon.
#nyt voi kutsua SQLAlchemyä importtaamalla db init_db.py:stä
#with app.app_context():
#    database.luonti()
#    database.create_Kirja("Avain", "Testi", "Title", "2025", "Publisher")
#    database.hae_tieto()

app.config['SECRET_KEY'] = '1234'

csrf = CSRFProtect(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search')
def search():
    return render_template("search.html")

@app.route('/add_reference', methods=['GET', 'POST'])
def add_reference():
    form = ReferenceForm()
    if form.validate_on_submit():
        #Poimitaan tiedot lomakkeesta
        ref_type = form.reference_type.data
        key = form.key.data
        author = form.author.data
        title = form.title.data
        year = form.year.data

        # Tarkistetaan viitteen tyyppi, poimitaan puuttuvat tiedot
        # ja kutsutaan vastaavaa funktiota tallentamaan tietokantaan
        if ref_type == "Book":
            publisher = form.publisher.data
            create_Kirja(key, author, title, year, publisher)
        elif ref_type == "Article":
            journal = form.journal.data
            volume = form.volume.data
            pages = form.pages.data
            create_artikkeli(key, author, title, year, journal, volume, pages)
        elif ref_type == "Inproceedings":
            booktitle = form.booktitle.data
            create_Konferenssijulkaisu(key, author, title, year, booktitle)

        return redirect('/')

    return render_template("add_reference.html", form=form)


@app.route('/reference_list')
def reference_list():
    return render_template("reference_list.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
