from django import forms
from .models import Item, Mozo


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("name", "description", "price")


class MozoForm(forms.ModelForm):
    class Meta:
        model = Mozo
        fields = ("nombre", "dni", "direccion", "telefono", "mail")
