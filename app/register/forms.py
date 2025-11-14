from flask_wtf import FlaskForm
from govuk_frontend_wtf.wtforms_widgets import (
    GovCheckboxInput,
    GovSubmitInput,
    GovTextInput,
)
from wtforms.fields import BooleanField, StringField, SubmitField
from wtforms.validators import InputRequired, ValidationError

from app.models import Register


class RegisterForm(FlaskForm):
    name = StringField(
        "Name",
        widget=GovTextInput(),
        validators=[InputRequired(message="Enter a name")],
    )
    submit: SubmitField = SubmitField("Save", widget=GovSubmitInput())

    def validate_name(self, field):
        if Register.query.filter_by(name=field.data).first():
            raise ValidationError("Name already in use")


class RegisterDeleteForm(FlaskForm):
    confirm = BooleanField(
        "I'm sure",
        widget=GovCheckboxInput(),
        validators=[InputRequired(message="Select if you want to delete this register")],
    )
    submit: SubmitField = SubmitField("Delete", widget=GovSubmitInput())
