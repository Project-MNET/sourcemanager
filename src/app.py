from io import BytesIO
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, send_file
from flask_wtf import CSRFProtect



from init_db import init, db
import database
from forms import ReferenceForm

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
        database.hae_tieto()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search')
def search():
    #Haku ja results ovat osana html templatea
    haku = False
    results = False
    attribuutti = "key"
    kirja = []
    artikkeli = []
    konferenssi = []

    haku_lahetetty = "query" in request.args or "types" in request.args
    if haku_lahetetty:
        haku = True
        query = request.args.get("query", "")
        types=request.args.getlist("types")
        attribuutti = request.args.get("attribuutti", "key")
        if not types:
            types = ["kaikki"]

    #Siirretään kaikki listat dictionarystä omiin listoihin:
        kaikki_dict = database.get(key = query, attribute = attribuutti)
        kirja = kaikki_dict["kirja"] if ("kirja" in types or "kaikki" in types) else []
        artikkeli = kaikki_dict["artikkeli"] if ("artikkeli" in types or "kaikki" in types) else []
        konferenssi = kaikki_dict["konferenssi"] \
            if ("konferenssi" in types or "kaikki" in types) else []

        if kirja or artikkeli or konferenssi:
            results = True
    return render_template("search.html", results = results, query = haku,
    types = types if haku_lahetetty else [], kirja = kirja, artikkeli=artikkeli,
    konferenssi=konferenssi)

@app.route('/add_reference', methods=['GET', 'POST'])
def add_reference():
    form = ReferenceForm()
    if form.validate_on_submit():
        #Poimitaan tiedot lomakkeesta
        ref_type = form.reference_type.data
        #Tallennetaan kaikki tieto dictionaryyn.
        ref_information = {}
        ref_information["type"] = form.reference_type.data
        ref_information["key"] = form.key.data
        ref_information["author"] = form.author.data
        ref_information["title"] = form.title.data
        ref_information["year"] = form.year.data
        ref_information["doi"] = form.doi.data
        # Tarkistetaan viitteen tyyppi, poimitaan puuttuvat tiedot
        # ja kutsutaan vastaavaa funktiota tallentamaan tietokantaan
        if ref_type == "Book":
            ref_information["publisher"] = form.publisher.data
            database.create_kirja(ref_information)
        elif ref_type == "Article":
            ref_information["journal"] = form.journal.data
            ref_information["volume"] = form.volume.data
            ref_information["pages"] = form.pages.data
            database.create_artikkeli(ref_information)
        elif ref_type == "Inproceedings":
            ref_information["booktitle"] = form.booktitle.data
            database.create_konferenssijulkaisu(ref_information)

        return redirect('/')

    error_list = []
    if form.errors:
        # Muotoillaan kenttäkohtaiset viestit listaksi
        for field_name, messages in form.errors.items():
            for msg in messages:
                error_list.append(f"{field_name}: {msg}")

    return render_template("add_reference.html", form=form, error_list=error_list)


@app.route('/reference_list', methods=["GET", "POST"])
def reference_list():
    references_dict = database.get()
    ref_list = [item for sublist in references_dict.values()
                for item in sublist]
    return render_template("reference_list.html", references=ref_list)


@app.route("/delete/<string:key>/<string:model>", methods=["POST"])
def delete_reference(key, model):
    database.delete(key, model)
    return redirect(request.referrer)


@app.route('/reference_list/download')
def download_references():
    bibtex_file = database.generate_bibtex()
    buffer = BytesIO(bibtex_file.encode('utf-8'))
    buffer.seek(0)
    return send_file(buffer,
                     as_attachment=True,
                     download_name="references.bib",
                     mimetype="application/x-bibtex")
