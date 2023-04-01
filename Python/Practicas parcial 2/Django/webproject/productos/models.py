from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    precio = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f'Producto {self.id} : {self.nombre}'

class DetallePedido(models.Model):
    cantidad = models.CharField(max_length=255)
    subtotal = models.BigIntegerField()
    numdetallepedido = models.ForeignKey(Producto,on_delete=models.SET_NULL,null = True) 
    def __str__(self) -> str:
        return f'DetallePedido {self.id} : {self.numdetallepedido}'
