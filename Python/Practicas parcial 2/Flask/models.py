from app import db

class Cemento(db.Model):
    id    = db.Column(db.Integer,primary_key=True)
    Marca = db.Column(db.String(255))

class Cheetos(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    Nombre = db.Column(db.String(255))
    Precio = db.Column(db.String(255))

class Dulces(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    Nombre = db.Column(db.String(255))
    Precio = db.Column(db.String(255))
    Marca = db.Column(db.String(255))
