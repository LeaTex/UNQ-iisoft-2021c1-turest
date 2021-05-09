from django.shortcuts import render
from administracion.models import Item
def home(request):
	return render(request, 'home.html', {'items':Item.objects.all()})
