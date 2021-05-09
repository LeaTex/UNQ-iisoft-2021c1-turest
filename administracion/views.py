from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Item
from .forms import ItemForm

def itemList(request):
	return render(request, 'admin/list.html', {'items':Item.objects.all()})

def itemChange(request, pk):
	return render(request, 'admin/itemChange.html', {'item': get_object_or_404(Item, pk=pk)})

def itemNew(request):
	if request.method == "POST":
		form = ItemForm(request.POST)
		if form.is_valid():
			item = form.save(commit=False)
			item.author = request.user
			item.published_date = timezone.now()
			item.save()
			return redirect('')
	else:
		return render(request, 'admin/itemNew.html', {'form': ItemForm()})
