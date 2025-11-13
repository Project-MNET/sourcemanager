import os
from flask import Flask
from flask import abort, redirect, render_template, request, session
from dotenv import load_dotenv
from forms import ReferenceForm


load_dotenv()

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search')
def search():
    return render_template("search.html")

@app.route('/add_reference')
def add_reference():
    form = ReferenceForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template("add_reference.html")

@app.route('/reference_list')
def reference_list():
    return render_template("reference_list.html")

if __name__ == '__main__':
    app.run(debug=True)
    