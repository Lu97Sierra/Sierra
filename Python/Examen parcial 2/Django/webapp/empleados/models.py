from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=255)
    puesto = models.CharField(max_length=255)
    salario = models.DecimalField(max_digits=10, decimal_places=2)