from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Item, Mozo, AsignacionMesa, Mesa, Sector
from .forms import ItemForm, MozoForm, AsignacionMesaForm, MesaForm, SectorForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .userGroupsFilter import *

@login_required
def home(request):
    if isAdmin(request.user):
        return render(request, 'admin/home.html', {'items': Item.objects.all()})
    elif isMozo(request.user):
        return render(request, 'mozo/home.html', {})
    else:
        return render(request, 'portal/home.html', {'items': Item.objects.all()})


@login_required
@user_passes_test(isAdmin)
def itemList(request):
    return render(request, 'admin/items.html', {'items': Item.objects.all()})


@login_required
@user_passes_test(isAdmin)
def itemInfo(request, pk):
    return render(request, 'admin/itemInfo.html', {'item': get_object_or_404(Item, pk=pk)})


@login_required
@user_passes_test(isAdmin)
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
@user_passes_test(isAdmin)
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
@user_passes_test(isAdmin)
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
@user_passes_test(isAdmin)
def mozoList(request):
    return render(request, 'admin/mozos.html', {'mozos': Mozo.objects.all()})


@login_required
@user_passes_test(isAdmin)
def asignacionNew(request):
    if request.method == "POST":
        form = AsignacionMesaForm(request.POST)
        if form.is_valid():
            asignacion = form.save(commit=False)
            asignacion.author = request.user
            asignacion.published_date = timezone.now()
            asignacion.save()
            return redirect('asignacionesList')
    else:
        return render(request, 'admin/asignacionMesa.html', {'form': AsignacionMesaForm()})


@login_required
@user_passes_test(isAdmin)
def asignacionesList(request):
    return render(request, 'admin/asignaciones.html', {'asignaciones': AsignacionMesa.objects.all()})


@login_required
@user_passes_test(isAdmin)
def mesaNew(request):
    if request.method == "POST":
        form = MesaForm(request.POST)
        if form.is_valid():
            mesa = form.save(commit=False)
            mesa.author = request.user
            mesa.published_date = timezone.now()
            mesa.save()
            return redirect('mesasList')
    else:
        return render(request, 'admin/mesaNew.html', {'form': MesaForm()})


@login_required
@user_passes_test(isAdmin)
def mesasList(request):
    return render(request, 'admin/mesasList.html', {'mesas': Mesa.objects.all(), 'sectores': Sector.objects.all()})


@login_required
@user_passes_test(isAdmin)
def sectorNew(request):
    if request.method == "POST":
        form = SectorForm(request.POST)
        if form.is_valid():
            sector = form.save(commit=False)
            sector.author = request.user
            sector.published_date = timezone.now()
            sector.save()
            return redirect('mesasList')
    else:
        return render(request, 'admin/sectorNew.html', {'form': SectorForm()})
