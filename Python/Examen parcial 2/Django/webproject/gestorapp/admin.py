from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Empresa, Domicilio, Empleado, Contacto, Producto

admin.site.register(Empresa)
admin.site.register(Domicilio)
admin.site.register(Empleado)
admin.site.register(Contacto)
admin.site.register(Producto)
