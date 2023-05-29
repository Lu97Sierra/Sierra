from flask import Blueprint, request, Flask, request, url_for, render_template, redirect, jsonify, make_response
from sqlalchemy import exc
from models import Proveedor,Producto,Imagen_Producto
#from app import db, bcrypt
from database import db
from encriptador import bcrypt
from auth import tokenCheck
from forms import FormProducto
import pdfkit
from fpdf import FPDF
config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
appproducto = Blueprint('appproducto',__name__,template_folder="templates")


@appproducto.route('/agregarproducto', methods=['POST','GET'])
@tokenCheck
def registro(usuario):
    mensaje = "Agregar mueble:"
    pro = FormProducto()
    if request.method == "POST":
        if pro.validate_on_submit():
            producto = {"nombreProducto":pro.nombreProducto.data, "desProducto":pro.desProducto.data}
            productoExist = Producto.query.filter_by(nombreProducto=producto['nombreProducto']).first()
            if not productoExist:
                agregar = Producto(nombreProducto=producto['nombreProducto'], desProducto=producto['desProducto'])
                try:
                    db.session.add(agregar)
                    db.session.commit()
                    mensaje = "Mueble registrado correctamente"
                except exc.SQLAlchemyError as e:
                    mensaje = print(e)
            else:
                mensaje="El mueble ya ha sido registrado"
            return render_template('Producto/agregarproducto.html', forma=pro, mensaje=mensaje)
    return render_template('Producto/agregarproducto.html', forma=pro, mensaje=mensaje)

@appproducto.route('/producto', methods=["GET"])
@tokenCheck
def getProducto(usuario):
    output=[]
    pros = Producto.query.all()
    return render_template('Producto/producto.html', pros=pros)


@appproducto.route('/producto/editar/<int:idProducto>', methods=['GET', 'POST'])
@tokenCheck
def editarproducto(usuario, idProducto):
    mensaje = "Editar informacion del mueble:"
    if usuario['admin']:
        juguete = Producto.query.get_or_404(idProducto)
        prod = FormProducto(obj=juguete)
        if request.method == "POST":
            if prod.validate_on_submit():
                prod.populate_obj(juguete)
                db.session.commit()
                return redirect(url_for('appproducto.getProducto'))
        return render_template('Producto/editarproducto.html', forma=prod,mensaje=mensaje)
    else:
        return render_template('admin.html')

@appproducto.route('/producto/eliminar/<int:idProducto>', methods=['GET', 'POST'])
@tokenCheck
def eliminarjuguete(usuario, idProducto):
    if usuario['admin']:
        prod = Producto.query.get_or_404(idProducto)
        db.session.delete(prod)
        db.session.commit()
        return redirect(url_for('appproducto.getProducto'))
    return render_template('admin.html')

@appproducto.route('/producto/detalle/<int:idProducto>', methods=['GET', 'POST'])
@tokenCheck
def detalleusuario(usuario, idProducto):
    try:
        if 'admin' in usuario:
            prod = Producto.query.get_or_404(idProducto)
            searchImage = Imagen_Producto.query.filter_by(idProducto=idProducto).first()
            if searchImage is not None:
                imag = searchImage.renderate_date
                return render_template('Producto/detalleproducto.html', producto=prod, imagen=imag)
            else:
                return render_template('404.html')
        else:
            return render_template('admin.html')
    except KeyError:
        return "Error: 'admin' no está en usuario", 500
    except Exception as e:
        return str(e), 500


