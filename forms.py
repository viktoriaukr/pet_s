from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL, Length



class AddPet(FlaskForm):
    """Form for adding a pet."""
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Pet species", choices=[("cat", "cat"), ("dog", "dog"), ("porcupine", "porcupine")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Pet age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes", validators=[Optional()])
    

class EditPet(FlaskForm):
    """Form for editing a pet information."""  
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Comments", validators=[Optional(), Length(min=10)])
    available = BooleanField("Available?")