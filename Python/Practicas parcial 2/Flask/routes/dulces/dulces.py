from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from models import Dulces
from forms import DulceForm
from app import db

appDulces = Blueprint('appDulces',__name__,template_folder='templates')

@appDulces.route('/indexd')
def inicio():
    dulces = Dulces.query.all()
    totalDulcess = Dulces.query.count()
    return render_template('indexd.html',dulces = dulces, totalDulcess = totalDulcess)

@appDulces.route('/agregard', methods=["GET","POST"])
def agregar():
    dulces = Dulces()
    dulcesForm = DulceForm(obj=dulces)
    if request.method == "POST":
        if dulcesForm.validate_on_submit():
            dulcesForm.populate_obj(dulces)
            db.session.add(dulces)
            db.session.commit()
            return redirect(url_for('appDulces.inicio'))
    return render_template('agregard.html',forma=dulcesForm)

@appDulces.route('/editard/<int:id>', methods=["GET","POST"])
def editar(id):
    dulces = Dulces.query.get_or_404(id)
    dulcesForm = DulceForm(obj=dulces)
    if request.method == "POST":
        if dulcesForm.validate_on_submit():
            dulcesForm.populate_obj(dulces)
            db.session.add(dulces)
            db.session.commit()
            return redirect(url_for('appDulces.inicio'))
    return render_template('editard.html',forma=dulcesForm)


@appDulces.route('/detalled/<int:id>')
def detalle(id):
    dulce = Dulces.query.get_or_404(id)
    return render_template('detalled.html',dulce = dulce)

@appDulces.route('/eliminard/<int:id>')
def eliminar(id):
    dulces = Dulces.query.get_or_404(id)
    db.session.delete(dulces)
    db.session.commit()
    return redirect(url_for('appDulces.inicio'))

# -----------------------------------------------------------------------------------------------------------------------------------------


appDulces2 = Blueprint('appDulces2',__name__,template_folder="templates")

@appDulces2.route('/dulces/agregar',methods={'POST'})
def agregarCheetos():
    try:
        json = request.get_json()
        dulces = Dulces()
        dulces.Nombre = json['Nombre']
        dulces.Precio = json['Precio']
        dulces.Marca = json['Marca']
        db.session.add(dulces)
        db.session.commit()
        return jsonify({"status":200, "mensaje":"dulces agregado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appDulces2.route('/dulces/editar',methods={"POST"})
def editarDulces():
    try:
        json = request.get_json()
        dulces = Dulces.query.get_or_404(json['id'])
        dulces.Nombre = json['Nombre']
        dulces.Precio = json['Precio']
        dulces.Marca = json['Marca']
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"dulces modificado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@appDulces2.route('/dulces/eliminar',methods={"POST"})
def eliminarDulces():
    try:
        json = request.get_json()
        dulces = Dulces.query.get_or_404(json['id'])
        db.session.delete(dulces)
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"dulces eliminado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@appDulces2.route('/dulces/obtener',methods={"GET"})
def obtenerDulces():
    dulces = Dulces.query.all()
    listaDulces=[]
    for p in dulces:
        dulces = {}
        dulces["Nombre"] = p.Nombre
        dulces["Precio"] = p.Precio
        dulces["Marca"] = p.Marca
        listaDulces.append(dulces)
    return jsonify({'Dulces':listaDulces})

    