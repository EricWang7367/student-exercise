from flask_wtf import FlaskForm
from govuk_frontend_wtf.wtforms_widgets import GovSubmitInput, GovTextInput
from wtforms.fields import StringField, SubmitField
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

