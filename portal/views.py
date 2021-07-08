from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from administracion.models import Item
from .cart import Cart


def home(request):
    if 'pedidos' in request.session:
        tienePedidos = len(request.session['pedidos']) > 0
    else:
        tienePedidos = False
    return render(request, 'portal/home.html', {'items': Item.objects.all(), 'pedidos': tienePedidos})


# @login_required
def itemView(request, pk):
    if request.method == "POST":
        Cart(request).agregarPedido()
        return redirect('home')
    else:
        return render(request, 'portal/itemView.html', {'item': get_object_or_404(Item, pk=pk)})


def cartView(request):
    carrito = Cart(request)
    lista = carrito.getItems()
    return render(request, 'portal/carrito.html', {'items': lista, 'total': carrito.getPrice(), "pedidos":len(lista)>0})


@login_required
def cartConfirm(request):
    Cart(request).registrar()
    return render(request, 'portal/confirmado.html', {})

def cartClear(request):
    Cart(request).limpiar()
    return redirect('cartView')
