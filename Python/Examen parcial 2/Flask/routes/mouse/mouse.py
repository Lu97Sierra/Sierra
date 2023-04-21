from flask import Blueprint, request, render_template, redirect, url_for
from models import Mouse
from app import db
from flask import Flask,request,render_template, url_for, jsonify, session
import logging
from werkzeug.utils import redirect
from werkzeug.exceptions import abort
app = Flask(__name__)
app.secret_key="llave_secreta"
logging.basicConfig(filename='error.log',level=logging.DEBUG)
appMouse = Blueprint('appMouse',__name__,template_folder="templates")

@appMouse.route('/mouses/agregar',methods={'POST'})
def agregarMouse():
    try:
        json = request.get_json()
        mouses = Mouse()
        mouses.id = json['id']
        mouses.Marca = json['Marca']
        db.session.add(mouses)
        db.session.commit()
        return jsonify({"status":200, "mensaje":"mouses agregado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appMouse.route('/mouses/editar',methods={"POST"})
def editarMouse():
    try:
        json = request.get_json()
        mouses = Mouse.query.get_or_404(json['id'])
        mouses.id = json['id']
        mouses.Marca = json['Marca']
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"mouses modificado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@appMouse.route('/mouses/eliminar',methods={"POST"})
def eliminarMouse():
    try:
        json = request.get_json()
        mouses = Mouse.query.get_or_404(json['id'])
        db.session.delete(mouses)
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"mouses eliminado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@appMouse.route('/mouses/obtener',methods={"GET"})
def obtenerMouses():
    mouses = Mouse.query.all()
    listamouse=[]
    for p in mouses:
        mouses = {}
        mouses["id"] = p.id
        mouses["Marca"] = p.Marca
        listamouse.append(mouses)
    return jsonify({'mouses':listamouse})