from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from administracion.models import Item


def home(request):
    if 'pedidos' in request.session:
        tienePedidos = len(request.session['pedidos']) > 0
    else:
        tienePedidos = False
    return render(request, 'portal/home.html', {'items': Item.objects.all(), 'pedidos': tienePedidos})


# @login_required
def itemView(request, pk):
    if request.method == "POST":
        pedido = (request.POST['item'], request.POST['cantidad'])
        if 'pedidos' in request.session:
            list = request.session['pedidos']
            list.append(pedido)
            request.session['pedidos'] = list
        else:
            request.session['pedidos'] = [pedido]
        return redirect('home')
    else:
        return render(request, 'portal/itemView.html', {'item': get_object_or_404(Item, pk=pk)})


def cartView(request):
    tienePedidos = len(request.session['pedidos']) > 0
    lista = []
    for id, cantidad in request.session['pedidos']:
        print("buscando", id)
        item = Item.objects.get(pk=int(id))
        lista.append((item, cantidad))
    return render(request, 'portal/carrito.html', {'items': lista, 'pedidos': tienePedidos})


@login_required
def cartConfirm(request):
    request.session['pedidos'] = []
    return render(request, 'portal/confirmado.html', {})
