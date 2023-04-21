from flask import Blueprint, request, render_template, redirect, url_for
from models import Teclado
from app import db
from flask import Flask,request,render_template, url_for, jsonify, session
import logging
from werkzeug.utils import redirect
from werkzeug.exceptions import abort
app = Flask(__name__)
app.secret_key="llave_secreta"
logging.basicConfig(filename='error.log',level=logging.DEBUG)
appTeclado = Blueprint('appTeclado',__name__,template_folder="templates")

@appTeclado.route('/teclados/agregar',methods={'POST'})
def agregarTeclados():
    try:
        json = request.get_json()
        teclados = Teclado()
        teclados.id = json['id']
        teclados.Marca = json['Marca']
        db.session.add(teclados)
        db.session.commit()
        return jsonify({"status":200, "mensaje":"teclados agregado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appTeclado.route('/teclados/editar',methods={"POST"})
def editarTeclados():
    try:
        json = request.get_json()
        teclados = Teclado.query.get_or_404(json['id'])
        teclados.id = json['id']
        teclados.Marca = json['Marca']
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"teclados modificado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@appTeclado.route('/teclados/eliminar',methods={"POST"})
def eliminarTeclados():
    try:
        json = request.get_json()
        teclados = Teclado.query.get_or_404(json['id'])
        db.session.delete(teclados)
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"teclados eliminado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@appTeclado.route('/teclados/obtener',methods={"GET"})
def obtenerTeclados():
    teclados = Teclado.query.all()
    listaTeclados=[]
    for p in teclados:
        teclados = {}
        teclados["id"] = p.id
        teclados["Marca"] = p.Marca
        listaTeclados.append(teclados)
    return jsonify({'mouses':listaTeclados})