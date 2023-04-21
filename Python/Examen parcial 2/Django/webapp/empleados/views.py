from django.shortcuts import render, redirect, get_object_or_404
from empleados.models import Empleado
from empleados.forms import empleadoform
# Create your views here.
def nuevoEmpleado(request):
    if request.method == 'POST':
        formaEmpleado = empleadoform(request.POST)
        if formaEmpleado.is_valid():
            formaEmpleado.save()
            return redirect('indexEmpleado')
    else:
        formaEmpleado = empleadoform()
    return render(request,'nuevo.html',{'formaEmpleado':formaEmpleado})

def editarEmpleado(request,id):
    empleado = get_object_or_404(Empleado,pk=id)
    if request.method == 'POST':
        formaEmpleado = empleadoform(request.POST,instance=empleado)
        if formaEmpleado.is_valid():
            formaEmpleado.save()
            return redirect('indexEmpleado')
    else:
        formaEmpleado = empleadoform(instance=empleado)
    return render(request,'editar.html',{'formaEmpleado':formaEmpleado})

def eliminarEmpleado(request, id):
    empleado = get_object_or_404(Empleado,pk=id)
    if empleado:
        empleado.delete()
    return redirect('indexEmpleado')

def detalleEmpleado(request,id):
    empleado = get_object_or_404(Empleado,pk=id)
    return render(request,'detalle.html',{'cliente':empleado})


