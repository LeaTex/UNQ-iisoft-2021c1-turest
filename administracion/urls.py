from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='panel'),
    path('items', views.itemList, name='itemList'),
    path('itemNew', views.itemNew, name='itemNew'),
    path('itemInfo/<int:pk>/', views.itemInfo, name='itemInfo'),
    path('itemChange/<int:pk>/', views.itemChange, name='itemChange'),
    path('mozos', views.mozoList, name='mozoList'),
    path('mozoNew', views.mozoNew, name='mozoNew'),
    path('asignacionSector', views.asignacionNew, name='asignacionNew'),
    path('asignaciones', views.asignacionesList, name='asignacionesList'),
    path('mesaNew', views.mesaNew, name='mesaNew'),
    path('mesas', views.mesasList, name='mesasList'),
    path('sectorNew', views.sectorNew, name='sectorNew')
]
