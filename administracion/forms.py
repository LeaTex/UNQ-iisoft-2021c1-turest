from django import forms
from .models import Item, Mozo, AsignacionMesa, Mesa


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("name", "description", "price")


class MozoForm(forms.ModelForm):
    class Meta:
        model = Mozo
        fields = ('nombre', 'dni', 'direccion', 'telefono', 'mail')


class AsignacionMesaForm(forms.ModelForm):
    class Meta:
        model = AsignacionMesa
        fields = ('mozo', 'sector')


class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ('mesa', 'capacidad')

