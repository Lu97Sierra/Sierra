from django.shortcuts import render
from clientes.models import Cliente
from empleados.models import Empleado
from productos.models import Producto 
# Create your views here.
def index(request):
    return render(request,'Bienvenido.html')

def indexClientes(request):
    noClientes = Cliente.objects.count()
    clientes = Cliente.objects.order_by('id')
    return render(request,'indexClientes.html',{'noClientes':noClientes, 'clientes':clientes})

def indexEmpleados(request):
    noClientes = Empleado.objects.count()
    clientes = Empleado.objects.order_by('id')
    return render(request,'indexEmpleados.html',{'noClientes':noClientes, 'clientes':clientes})

def indexProductos(request):
    noClientes = Producto.objects.count()
    clientes = Producto.objects.order_by('id')
    return render(request,'indexProductos.html',{'noClientes':noClientes, 'clientes':clientes})
