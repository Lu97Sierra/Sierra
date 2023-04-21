from app import db

class Gabinete(db.Model):
    id    = db.Column(db.Integer,primary_key=True)
    Marca = db.Column(db.String(255))

class Mouse(db.Model):
    id    = db.Column(db.Integer,primary_key=True)
    Marca = db.Column(db.String(255))

class Pantalla(db.Model):
    id    = db.Column(db.Integer,primary_key=True)
    Marca = db.Column(db.String(255))

class Silla(db.Model):
    id    = db.Column(db.Integer,primary_key=True)
    Marca = db.Column(db.String(255))

class Teclado(db.Model):
    id    = db.Column(db.Integer,primary_key=True)
    Marca = db.Column(db.String(255))