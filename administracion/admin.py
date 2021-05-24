from django.contrib import admin
from .models import Item, Mozo, AsignacionMesa, Mesa, Sector

# Register your models here.
admin.site.register(Item)
admin.site.register(Mozo)
admin.site.register(AsignacionMesa)
admin.site.register(Mesa)
admin.site.register(Sector)