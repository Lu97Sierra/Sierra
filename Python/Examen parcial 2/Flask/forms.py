from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class GabineteForm(FlaskForm):
    id = StringField('Numero',validators=[DataRequired()])
    marca = StringField('Marca',validators=[DataRequired()])
    enviar = SubmitField('Enviar')

class PantallaForm(FlaskForm):
    id = StringField('Numero',validators=[DataRequired()])
    marca = StringField('Marca',validators=[DataRequired()])
    enviar = SubmitField('Enviar')