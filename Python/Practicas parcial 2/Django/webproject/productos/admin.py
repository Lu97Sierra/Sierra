from django.contrib import admin
from productos.models import Producto,DetallePedido
# Register your models here.
admin.site.register(Producto)
admin.site.register(DetallePedido)
