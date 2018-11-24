from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from wtforms.validators import validationError
from ..models import User