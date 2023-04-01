from flask import Blueprint, request, render_template, redirect, url_for
from models import Cemento
from forms import CementoForm
from app import db

appCemento = Blueprint('appCemento',__name__,template_folder='templates')

@appCemento.route('/index')
def inicio():
    cementos = Cemento.query.all()
    totalCementos = Cemento.query.count()
    return render_template('index.html',cementos = cementos, totalCementos = totalCementos)

@appCemento.route('/agregar', methods=["GET","POST"])
def agregar():
    cemento = Cemento()
    cementoForm = CementoForm(obj=cemento)
    if request.method == "POST":
        if cementoForm.validate_on_submit():
            cementoForm.populate_obj(cemento)
            db.session.add(cemento)
            db.session.commit()
            return redirect(url_for('appCemento.inicio'))
    return render_template('agregar.html',forma=cementoForm)

@appCemento.route('/editar/<int:id>', methods=["GET","POST"])
def editar(id):
    cemento = Cemento.query.get_or_404(id)
    cementoForm = CementoForm(obj=cemento)
    if request.method == "POST":
        if cementoForm.validate_on_submit():
            cementoForm.populate_obj(cemento)
            db.session.add(cemento)
            db.session.commit()
            return redirect(url_for('appCemento.inicio'))
    return render_template('editar.html',forma=cementoForm)


@appCemento.route('/detalle/<int:id>')
def detalle(id):
    cemento = Cemento.query.get_or_404(id)
    return render_template('detalle.html',cemento = cemento)

@appCemento.route('/eliminar/<int:id>')
def eliminar(id):
    cemento = Cemento.query.get_or_404(id)
    db.session.delete(cemento)
    db.session.commit()
    return redirect(url_for('appCemento.inicio'))


    