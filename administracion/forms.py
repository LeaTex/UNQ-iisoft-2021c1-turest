from django import forms
from .models import Item, Mozo, AsignacionMesa


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("name", "description", "price")


class MozoForm(forms.ModelForm):
<<<<<<< HEAD
	class Meta:
		model = Mozo
		fields = ('nombre', 'dni', 'direccion', 'telefono', 'mail')

class AsignacionMesaForm(forms.ModelForm):
	class Meta:
		model = AsignacionMesa
		fields = ('mozo', 'sector')
=======
    class Meta:
        model = Mozo
        fields = ("nombre", "dni", "direccion", "telefono", "mail")
>>>>>>> 4c2fffbf20e1c66234eb01a15ebed24daebafb1f
