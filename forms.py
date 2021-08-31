""" app forms """

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TexatAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField(
        "Pet Name",
        validators = [InputRequired()],
    )

    species = SelectField(
        "Species",
        choices = [("cat", "Cat"), ("dog","Dog"), ("porcupine","Porcupine")],
    )

    photo_url = StringField(
        "Photo URL",
         validators = [Optional(), NumberRange(min=0, max=30)],
    )

    age = IntegerField(
        "Age",
        validators = [Optional(), NumberRange(min = 0 , max = 30)],
    )

    notes = TexatAreaField(
        "Comments",
        validators = [Optional(), NumberRange(min = 0, max = 30)],
    )

    class EditPetForm(FlaskForm):
        """Form for editing an exiting pet"""

        Photo_url = StringField(
            "Photo URL", 

            validators = [Optional(), URL()],

        )

        notes = TexatAreaField(
            "Comments",
             validators = [Optional(), Length(min = 10)],
        )

        available = BooleanField("Available?")

    

