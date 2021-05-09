from django.urls import path
from . import views

urlpatterns = [
	path('', views.itemList, name='item_list'),
	path('itemChange/<int:pk>/', views.itemChange, name='itemChange'),
]
