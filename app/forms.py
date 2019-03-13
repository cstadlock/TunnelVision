from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtfpeewee.orm import model_form
from app.models.models import Bow

class DesignForm(model_form(Bow, FlaskForm)):
    bow_type = StringField()
    amountNeeded = IntegerField()
    