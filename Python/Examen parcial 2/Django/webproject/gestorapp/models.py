from django.db import models

# Create your models here.
from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Domicilio(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    calle = models.CharField(max_length=100)
    numero = models.IntegerField()
    ciudad = models.CharField(max_length=100)

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

class Contacto(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

