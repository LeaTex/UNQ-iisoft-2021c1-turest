from django.shortcuts import render, get_object_or_404, redirect
from administracion.models import Item


def home(request):
    return render(request, 'portal/home.html', {'items': Item.objects.all(), 'pedidos':request.session.get('pedidos', [])})


#@login_required
def itemView(request, pk):
    if request.method == "POST":
        pedido = (request.POST['item'], request.POST['cantidad'])
        if 'pedidos' in request.session:
            request.session['pedidos'].append(pedido)
        else:
            request.session['pedidos'] = [pedido]
        return redirect('home')
    else:
        return render(request, 'portal/itemView.html', {'item': get_object_or_404(Item, pk=pk)})
