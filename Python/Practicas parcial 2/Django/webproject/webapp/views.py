from django.shortcuts import render
from clientes.models import Pedido, Cliente
from ventas.models import Venta
# Create your views here.
def indexclientes(request):
    noPedidos = Pedido.objects.count()
    pedidos = Pedido.objects.order_by('id')

    noClientes = Cliente.objects.count()
    clientes = Cliente.objects.order_by('id')

    noVentas = Venta.objects.count()
    ventas = Venta.objects.order_by('id')

    return render(request,'indexclientes.html',{'noPedidos':noPedidos, 'pedidos':pedidos,
                                        'noVentas':noVentas, 'ventas':ventas,
                                        'noClientes':noClientes, 'clientes':clientes})





