from django.shortcuts import render, redirect, get_object_or_404
from clientes.models import Cliente
from clientes.forms import clienteform
# Create your views here.
def nuevoCliente(request):
    if request.method == 'POST':
        formaCliente = clienteform(request.POST)
        if formaCliente.is_valid():
            formaCliente.save()
            return redirect('indexClientes')
    else:
        formaCliente = clienteform()
    return render(request,'nuevo.html',{'formaClientes':formaCliente})

def editarCliente(request,id):
    cliente = get_object_or_404(Cliente,pk=id)
    if request.method == 'POST':
        formaCliente = clienteform(request.POST,instance=cliente)
        if formaCliente.is_valid():
            formaCliente.save()
            return redirect('indexClientes')
    else:
        formaCliente = clienteform(instance=cliente)
    return render(request,'editar.html',{'formaClientes':formaCliente})

def eliminarCliente(request, id):
    cliente = get_object_or_404(Cliente,pk=id)
    if cliente:
        cliente.delete()
    return redirect('indexClientes')

def detalleCliente(request,id):
    cliente = get_object_or_404(Cliente,pk=id)
    return render(request,'detalle.html',{'cliente':cliente})

