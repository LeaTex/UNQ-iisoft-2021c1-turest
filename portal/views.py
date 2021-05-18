from django.shortcuts import render
from administracion.models import Item

def home(request):
    return render(request, 'portal/home.html', {'items':Item.objects.all()})
