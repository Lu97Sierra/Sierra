from flask import Blueprint, request,jsonify
from models import Cheetos
from app import db

appCheetos = Blueprint('appCheetos',__name__,template_folder="templates")

@appCheetos.route('/cheetos/agregar',methods={'POST'})
def agregarCheetos():
    try:
        json = request.get_json()
        cheetos = Cheetos()
        cheetos.Nombre = json['Nombre']
        cheetos.Precio = json['Precio']
        db.session.add(cheetos)
        db.session.commit()
        return jsonify({"status":200, "mensaje":"Cheetos agregado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appCheetos.route('/cheetos/editar',methods={"POST"})
def editarCheetos():
    try:
        json = request.get_json()
        cheetos = Cheetos.query.get_or_404(json['id'])
        cheetos.Nombre = json['Nombre']
        cheetos.Precio = json['Precio']
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"Cheetos modificado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@appCheetos.route('/cheetos/eliminar',methods={"POST"})
def eliminarCheetos():
    try:
        json = request.get_json()
        cheetos = Cheetos.query.get_or_404(json['id'])
        db.session.delete(Cheetos)
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"Cheetos eliminado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@appCheetos.route('/cheetos/obtener',methods={"GET"})
def obtenerCheetoss():
    Cheetoss = Cheetos.query.all()
    listaCheetoss=[]
    for p in Cheetoss:
        cheetos = {}
        cheetos["Nombre"] = p.nombre
        cheetos["Precio"] = p.precio
        listaCheetoss.append(Cheetos)
    return jsonify({'Cheetos':listaCheetoss})