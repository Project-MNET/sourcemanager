from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, ValidationError, IntegerField
from wtforms.validators import DataRequired, Length, Optional, NumberRange
from .database import unique_key_check

class ReferenceForm(FlaskForm):
    reference_type = SelectField(
        'Viitteen tyyppi',
        choices=[('Book','Book'), ('Article','Article'), ('Inproceedings','Inproceedings')]
    )
    key = StringField('KEY', validators=[DataRequired(message='Key on pakollinen'),
    Length(max=64, message='Key ei voi olla yli 64 merkkiä')])
    author = StringField('Author', validators=[DataRequired(message='Author on pakollinen'),
    Length(max=512, message='Author ei voi olla yli 512 merkkiä')])
    # Huom tämä täytyy vaihtaa ehkä suuremmaksi, author voi olla pitkä lista
    title = StringField('Title', validators=[DataRequired(message='Title on pakollinen'),
    Length(max=256, message='Title ei voi olla yli 256 merkkiä')])
    year = IntegerField('Year', validators=[DataRequired(message='Year on pakollinen, 1-3000'),
    NumberRange(min=1, max=3000, message='Year tulee olla välillä 1-3000')])
    publisher = StringField('Publisher', validators=[Optional(),
    Length(max=256, message='Publisher ei voi olla yli 256 merkkiä')])        # Book only
    journal = StringField('Journal', validators=[Optional(),
    Length(max=256, message='Journal ei voi olla yli 256 merkkiä')])            # Article only
    volume = StringField('Volume', validators=[Optional(),
    Length(max=256, message='Volume ei voi olla yli 256 merkkiä')])              # Article only
    pages = StringField('Pages', validators=[Optional(),
    Length(max=256, message='Pages ei voi olla yli 256 merkkiä')])                # Article only
    booktitle = StringField('Booktitle', validators=[Optional(),
    Length(max=256, message='Booktitle ei voi olla yli 256 merkkiä')])        # Inproceedings only
    submit = SubmitField('Lisää viite')


    def validate_key(self, field):
        val = (field.data or '').strip()
        if not val:
            return
        if not unique_key_check(val):
            raise ValidationError('Tämä key on jo käytössä (duplikaatti)!')
