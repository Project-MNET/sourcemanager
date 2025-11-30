from dotenv import load_dotenv
from flask import Flask, redirect, render_template
from flask_wtf import CSRFProtect

from .init_db import init, db
from .import database
from .forms import ReferenceForm

load_dotenv()

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

app.config['SECRET_KEY'] = '1234'

init(app) #tämä yhdistää dbn flask applikaatioon.
#nyt voi kutsua SQLAlchemyä importtaamalla db init_db.py:stä

csrf = CSRFProtect(app)

with app.app_context():
    db.create_all()

def initialize_database():
    with app.app_context():
        database.luonti()
        database.create_kirja("Avain", "Testi",
     "Title", "2025", "Publisher")
        database.hae_tieto()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search')
def search():
    #Haku ja results ovat osana html templatea
    haku = False
    results = False
    query = request.args.get("query")

    #Siirretään kaikki listat dictionarystä omiin listoihin:
    kaikki_dict = database.get(key = query)
    kirja = kaikki_dict["kirja"]
    artikkeli = kaikki_dict["artikkeli"]
    konferenssi = kaikki_dict["konferenssi"]
    #Tarkistetaan tapahtuiko query oikeasti
    if query:
        haku = True
        #Tarkistetaan oliko queryssä vain tyhjiä listoja.
        if any(list for list in kaikki_dict.values()):
            results = True
    return render_template("search.html", results = results, query = haku,
                    kirja = kirja, artikkeli=artikkeli, konferenssi=konferenssi)

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
            database.create_kirja(key, author, title, year, publisher)
        elif ref_type == "Article":
            journal = form.journal.data
            volume = form.volume.data
            pages = form.pages.data
            database.create_artikkeli(key, author, title, year, journal, volume, pages)
        elif ref_type == "Inproceedings":
            booktitle = form.booktitle.data
            database.create_konferenssijulkaisu(key, author, title, year, booktitle)

        return redirect('/')

    return render_template("add_reference.html",
            form=form)


@app.route('/reference_list')
def reference_list():
    references_dict = database.get()
    ref_list = [item for sublist in references_dict.values()
                for item in sublist]
    return render_template("reference_list.html", references=ref_list)

if __name__ == "__main__":
    initialize_database()
    app.run(host="0.0.0.0", port=5001)
