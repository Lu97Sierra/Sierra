from django.db import models

# Create your models here.

class Venta(models.Model):
    fecha = models.CharField(max_length=255)
    monto = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f'Venta {self.id} : {self.monto}'
