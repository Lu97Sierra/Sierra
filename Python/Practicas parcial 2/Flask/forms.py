from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CementoForm(FlaskForm):
    marca = StringField('Nombre',validators=[DataRequired()])
    enviar = SubmitField('Enviar')

class DulceForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()])
    precio = StringField('Precio')
    marca = StringField('Marca')
    enviar = SubmitField('Enviar')