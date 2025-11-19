from flask import Flask, redirect, render_template
from flask_wtf import CSRFProtect
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from src.forms import ReferenceForm

from src.init_db import db, init
from src import database
load_dotenv()

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)
#init(app) #tämä yhdistää dbn flask applikaatioon.
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
        return redirect('/')
    return render_template("add_reference.html", form=form)

@app.route('/reference_list')
def reference_list():
    return render_template("reference_list.html")

if __name__ == '__main__':
    app.run(debug=True)
