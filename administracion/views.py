from django.shortcuts import render, get_object_or_404
from .models import Item

def itemList(request):
	return render(request, 'admin/list.html', {'items':Item.objects.all()})

def itemChange(request, pk):
    return render(request, 'admin/itemChange.html', {'item': get_object_or_404(Item, pk=pk)})
