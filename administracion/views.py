from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Item, Mozo
from .forms import ItemForm, MozoForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'admin/home.html', {'items': Item.objects.all()})


@login_required
def itemList(request):
    return render(request, 'admin/items.html', {'items': Item.objects.all()})


@login_required
def itemInfo(request, pk):
    return render(request, 'admin/itemInfo.html', {'item': get_object_or_404(Item, pk=pk)})


@login_required
def itemChange(request, pk):
    item = get_object_or_404(Item, pk=pk)
    form = ItemForm(request.POST, instance=item)
    if request.method == "POST":
        if form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.published_date = timezone.now()
            item.save()
            return redirect('itemInfo', pk=item.pk)
    else:
        return render(request, 'admin/itemChange.html', {'form': form})


@login_required
def itemNew(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.published_date = timezone.now()
            item.save()
            return redirect('itemInfo', pk=item.pk)
    else:
        return render(request, 'admin/itemNew.html', {'form': ItemForm()})


@login_required
def mozoNew(request):
    if request.method == "POST":
        form = MozoForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.published_date = timezone.now()
            item.save()
            return redirect('mozoList')
    else:
        return render(request, 'admin/mozoNew.html', {'form': MozoForm()})


@login_required
def mozoList(request):
    return render(request, 'admin/mozos.html', {'mozos': Mozo.objects.all()})
