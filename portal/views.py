from django.shortcuts import render, get_object_or_404, redirect
from administracion.models import Item


def home(request):
    tienePedido = 'pedidos' in request.session
    return render(request, 'portal/home.html', {'items': Item.objects.all(), 'pedidos': tienePedido})

def cartView(request):
    pedidos = []
    for id, cantidad in  request.session['pedidos']:
        pass
    return render(request, 'portal/carrito.html', {'pedidos': pedidos})


#@login_required
def itemView(request, pk):
    if request.method == "POST":
        pedido = (request.POST['item'], request.POST['cantidad'])
        if 'pedidos' in request.session:
            print("el pedido", request.session['pedidos'])
            lista = request.session['pedidos']
            lista.append(pedido)
            request.session['pedidos'] = lista
            print("el pedido", request.session['pedidos'])
        else:
            request.session['pedidos'] = [pedido]
        return redirect('home')
    else:
        return render(request, 'portal/itemView.html', {'item': get_object_or_404(Item, pk=pk)})
