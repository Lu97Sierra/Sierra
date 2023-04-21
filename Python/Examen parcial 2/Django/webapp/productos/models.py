from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria,on_delete=models.SET_NULL,null=True)