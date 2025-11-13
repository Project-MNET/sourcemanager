from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length

class ReferenceForm(FlaskForm):
    reference_type = SelectField(
        'Viitteen tyyppi',
        choices=[('Book','Book'), ('Article','Article'), ('Inproceedings','Inproceedings')]
    )
    key = StringField('KEY')
    author = StringField('Author')
    title = StringField('Title')
    year = StringField('Year')
    publisher = StringField('Publisher')        # Book only
    journal = StringField('Journal')            # Article only
    volume = StringField('Volume')              # Article only
    pages = StringField('Pages')                # Article only
    booktitle = StringField('Booktitle')        # Inproceedings only
    submit = SubmitField('Lisää viite')
    