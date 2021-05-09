from django.shortcuts import render
from .models import Item

def itemList(request):
	return render(request, 'list.html', {'items':Item.objects.all()})
