"""
URL configuration for webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestorapp.views import *
from clientes.views import *
from empleados.views import *
from productos.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('indexEmpleados',indexEmpleados,name='indexEmpleados'),
    path('nuevoEmpleado',nuevoEmpleado),
    path('editarEmpleado/<int:id>',editarEmpleado),
    path('eliminarEmpleado/<int:id>',eliminarEmpleado),
    path('detalleEmpleado/<int:id>',detalleEmpleado),
    path('indexClientes',indexClientes,name='indexClientes'),
    path('nuevoCliente',nuevoCliente),
    path('editarCliente/<int:id>',editarCliente),
    path('eliminarCliente/<int:id>',eliminarCliente),
    path('detalleCliente/<int:id>',detalleCliente),
    path('indexProductos',indexProductos,name='indexProductos'),
    path('nuevoProducto',nuevoProducto),
    path('editarProducto/<int:id>',editarProducto),
    path('eliminarProducto/<int:id>',eliminarProducto),
    path('detalleProducto/<int:id>',detalleProducto)
]
