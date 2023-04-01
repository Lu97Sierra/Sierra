from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f'Empleado {self.id} : {self.nombre}'

