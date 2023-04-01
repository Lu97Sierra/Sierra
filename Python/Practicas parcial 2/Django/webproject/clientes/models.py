from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f'Cliente {self.id} : {self.nombre}'

class Pedido(models.Model):
    fecha = models.CharField(max_length=255)
    monto = models.BigIntegerField()
    telefono = models.CharField(max_length=255)
    numcliente = models.ForeignKey(Cliente,on_delete=models.SET_NULL,null = True) 
    def __str__(self) -> str:
        return f'Pedido {self.id} : {self.telefono}'
