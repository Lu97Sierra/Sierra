from django.contrib import admin

from clientes.models import Cliente, Pedido
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Pedido)
