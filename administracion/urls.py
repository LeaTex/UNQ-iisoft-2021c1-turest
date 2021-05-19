from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
	path('', views.home, name='panel'),
	path('items', views.itemList, name='itemList'),
	path('itemNew', views.itemNew, name='itemNew'),
	path('itemInfo/<int:pk>/', views.itemInfo, name='itemInfo'),
	path('itemChange/<int:pk>/', views.itemChange, name='itemChange'),
	path('mozos', views.mozoList, name='mozoList'),
	path('mozoNew', views.mozoNew, name='mozoNew'),
	path('asignacionMesa', views.asignacionNew, name='asignacionNew'),
	path('asignaciones', views.asignacionesList, name='asignacionesList'),

=======
    path("", views.home, name="panel"),
    path("items", views.itemList, name="itemList"),
    path("itemNew", views.itemNew, name="itemNew"),
    path("itemInfo/<int:pk>/", views.itemInfo, name="itemInfo"),
    path("itemChange/<int:pk>/", views.itemChange, name="itemChange"),
    path("mozos", views.mozoList, name="mozoList"),
    path("mozoNew", views.mozoNew, name="mozoNew"),
>>>>>>> 4c2fffbf20e1c66234eb01a15ebed24daebafb1f
]
