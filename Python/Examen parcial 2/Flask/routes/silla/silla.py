from flask import Blueprint, request, render_template, redirect, url_for
from models import Silla
from app import db
from flask import Flask,request,render_template, url_for, jsonify, session
import logging
from werkzeug.utils import redirect
from werkzeug.exceptions import abort
app = Flask(__name__)
app.secret_key="llave_secreta"
logging.basicConfig(filename='error.log',level=logging.DEBUG)
appSilla = Blueprint('appSilla',__name__,template_folder="templates")

@appSilla.route('/sillas/agregar',methods={'POST'})
def agregarSillas():
    try:
        json = request.get_json()
        sillas = Silla()
        sillas.id = json['id']
        sillas.Marca = json['Marca']
        db.session.add(sillas)
        db.session.commit()
        return jsonify({"status":200, "mensaje":"sillas agregado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appSilla.route('/sillas/editar',methods={"POST"})
def editarSillas():
    try:
        json = request.get_json()
        sillas = Silla.query.get_or_404(json['id'])
        sillas.id = json['id']
        sillas.Marca = json['Marca']
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"sillas modificado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@appSilla.route('/sillas/eliminar',methods={"POST"})
def eliminarSillas():
    try:
        json = request.get_json()
        sillas = Silla.query.get_or_404(json['id'])
        db.session.delete(sillas)
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"sillas eliminado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@appSilla.route('/sillas/obtener',methods={"GET"})
def obtenerSillas():
    sillas = Silla.query.all()
    listaSillas=[]
    for p in sillas:
        sillas = {}
        sillas["id"] = p.id
        sillas["Marca"] = p.Marca
        listaSillas.append(sillas)
    return jsonify({'mouses':listaSillas})