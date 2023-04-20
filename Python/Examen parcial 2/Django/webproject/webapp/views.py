from django.shortcuts import render

# Create your views here.
from gestorapp.models import Empresa, Empleado, Producto

def empresa_index(request):
    empresas = Empresa.objects.all()
    return render(request, 'webapp/empresa_index.html', {'empresas': empresas})
def empleado_index(request):
    empleado = Empleado.objects.all()
    return render(request, 'webapp/empleado_index.html', {'empleado': empleado})
def producto_index(request):
    producto = Producto.objects.all()
    return render(request, 'webapp/producto_index.html', {'producto': producto})
