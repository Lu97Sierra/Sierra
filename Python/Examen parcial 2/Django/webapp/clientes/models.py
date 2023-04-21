from django.db import models

# Create your models here.


class Pedido(models.Model):
    fecha = models.DateTimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    pedidos = models.ForeignKey(Pedido,on_delete=models.SET_NULL,null=True)