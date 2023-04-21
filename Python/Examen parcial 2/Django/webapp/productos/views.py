from django.shortcuts import render, redirect, get_object_or_404
from productos.models import Producto
from productos.forms import productoform
# Create your views here.
def nuevoProducto(request):
    if request.method == 'POST':
        formaProducto = productoform(request.POST)
        if formaProducto.is_valid():
            formaProducto.save()
            return redirect('indexProducto')
    else:
        formaProducto = productoform()
    return render(request,'nuevo.html',{'formaProducto':formaProducto})

def editarProducto(request,id):
    producto = get_object_or_404(Producto,pk=id)
    if request.method == 'POST':
        formaProducto = productoform(request.POST,instance=producto)
        if formaProducto.is_valid():
            formaProducto.save()
            return redirect('indexProducto')
    else:
        formaProducto = productoform(instance=producto)
    return render(request,'editar.html',{'formaProducto':formaProducto})

def eliminarProducto(request, id):
    producto = get_object_or_404(Producto,pk=id)
    if producto:
        producto.delete()
    return redirect('indexProducto')

def detalleProducto(request,id):
    producto = get_object_or_404(Producto,pk=id)
    return render(request,'detalle.html',{'producto':producto})



