from flask import Blueprint, request, render_template, redirect, url_for
from models import Gabinete
from forms import GabineteForm
from app import db
from flask import Flask,request,render_template, url_for, jsonify, session
import logging
from werkzeug.utils import redirect
from werkzeug.exceptions import abort
app = Flask(__name__)
app.secret_key="llave_secreta"
logging.basicConfig(filename='error.log',level=logging.DEBUG)

appGabinete = Blueprint('appGabinete',__name__,template_folder='templates')

@appGabinete.route('/index')
def inicio():
    gabinetes = Gabinete.query.all()
    totalGabinetes = Gabinete.query.count()
    return render_template('index.html',gabinetes = gabinetes, totalGabinetes = totalGabinetes)

@appGabinete.route('/agregar', methods=["GET","POST"])
def agregar():
    gabinetes = Gabinete()
    gabineteForm = GabineteForm(obj=gabinetes)
    if request.method == "POST":
        if gabineteForm.validate_on_submit():
            gabineteForm.populate_obj(gabinetes)
            db.session.add(gabinetes)
            db.session.commit()
            return redirect(url_for('appGabinete.inicio'))
    return render_template('agregar.html',forma=gabineteForm)

@appGabinete.route('/editar/<int:id>', methods=["GET","POST"])
def editar(id):
    gabinetes = Gabinete.query.get_or_404(id)
    gabineteForm = GabineteForm(obj=gabinetes)
    if request.method == "POST":
        if gabineteForm.validate_on_submit():
            gabineteForm.populate_obj(gabinetes)
            db.session.add(gabinetes)
            db.session.commit()
            return redirect(url_for('appGabinete.inicio'))
    return render_template('editar.html',forma=gabineteForm)


@appGabinete.route('/detalle/<int:id>')
def detalle(id):
    gabinetes = Gabinete.query.get_or_404(id)
    return render_template('detalle.html',gabinetes = gabinetes)

@appGabinete.route('/eliminar/<int:id>')
def eliminar(id):
    gabinetes = Gabinete.query.get_or_404(id)
    db.session.delete(gabinetes)
    db.session.commit()
    return redirect(url_for('appGabinete.inicio'))

@app.errorhandler(404)
def paginaNoEncontrada(error):
    return render_template('error404.html', error=error),404

#----------------------------------------------------------------------------
appGabinete2 = Blueprint('appGabinete2',__name__,template_folder="templates")

@appGabinete2.route('/dulces/agregar',methods={'POST'})
def agregarCheetos():
    try:
        json = request.get_json()
        gabinetes = Gabinete()
        gabinetes.id = json['id']
        gabinetes.Marca = json['Marca']
        db.session.add(gabinetes)
        db.session.commit()
        return jsonify({"status":200, "mensaje":"gabinetes agregado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appGabinete2.route('/gabinetes/editar',methods={"POST"})
def editarDulces():
    try:
        json = request.get_json()
        gabinetes = Gabinete.query.get_or_404(json['id'])
        gabinetes.id = json['id']
        gabinetes.Marca = json['Marca']
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"gabinetes modificado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@appGabinete2.route('/gabinetes/eliminar',methods={"POST"})
def eliminarGabinetes():
    try:
        json = request.get_json()
        gabinetes = Gabinete.query.get_or_404(json['id'])
        db.session.delete(gabinetes)
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"gabinetes eliminado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@appGabinete2.route('/gabinetes/obtener',methods={"GET"})
def obtenerGabinetes():
    gabinetes = Gabinete.query.all()
    listaGabinetes=[]
    for p in gabinetes:
        gabinetes = {}
        gabinetes["id"] = p.id
        gabinetes["Marca"] = p.Marca
        listaGabinetes.append(gabinetes)
    return jsonify({'Gabinetes':listaGabinetes})