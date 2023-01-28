from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, NumberRange, Optional, URL, Length

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[
        InputRequired(message="Pet Must Have Name")],)
    species = SelectField("Species", choices=[("cat", "cat"), ("dog", "dog"), ("porcupine", "porcupine"), ("bird", "bird"), ("reptile", "reptile")],)
    photo_url = StringField( validators=[Optional(), URL()],)
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=33)],)
    notes = TextAreaField("Comments", validators=[Optional(), Length(min=8)],)


class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL", validators=[Optional(), URL()],)
    notes = TextAreaField("Comments", validators=[Optional(), Length(min=8)],)
    available = BooleanField("Available?")