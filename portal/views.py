from django.shortcuts import render, get_object_or_404, redirect
from administracion.models import Item


def home(request):
    return render(request, 'portal/home.html', {'items': Item.objects.all()})


#@login_required
def itemView(request, pk):
    return render(request, 'portal/itemView.html', {'item': get_object_or_404 (Item, pk=pk)})