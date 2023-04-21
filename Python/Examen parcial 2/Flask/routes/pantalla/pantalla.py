from flask import Blueprint, request, render_template, redirect, url_for
from models import Pantalla
from app import db
from flask import Flask,request,render_template, url_for, jsonify, session
import logging
from werkzeug.utils import redirect
from werkzeug.exceptions import abort
app = Flask(__name__)
app.secret_key="llave_secreta"
logging.basicConfig(filename='error.log',level=logging.DEBUG)
appPantalla = Blueprint('appPantalla',__name__,template_folder="templates")

@appPantalla.route('/pantallas/agregar',methods={'POST'})
def agregarPantallas():
    try:
        json = request.get_json()
        pantallas = Pantalla()
        pantallas.id = json['id']
        pantallas.Marca = json['Marca']
        db.session.add(pantallas)
        db.session.commit()
        return jsonify({"status":200, "mensaje":"pantallas agregado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appPantalla.route('/pantallas/editar',methods={"POST"})
def editarPantallas():
    try:
        json = request.get_json()
        pantallas = Pantalla.query.get_or_404(json['id'])
        pantallas.id = json['id']
        pantallas.Marca = json['Marca']
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"pantallas modificado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@appPantalla.route('/pantallas/eliminar',methods={"POST"})
def eliminarPantallas():
    try:
        json = request.get_json()
        pantallas = Pantalla.query.get_or_404(json['id'])
        db.session.delete(pantallas)
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"pantallas eliminado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@appPantalla.route('/pantallas/obtener',methods={"GET"})
def obtenerPantallas():
    pantallas = Pantalla.query.all()
    listaPantallas=[]
    for p in pantallas:
        pantallas = {}
        pantallas["id"] = p.id
        pantallas["Marca"] = p.Marca
        listaPantallas.append(pantallas)
    return jsonify({'mouses':listaPantallas})