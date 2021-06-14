from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.home, name="home"),
    path("login", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout", LogoutView.as_view(template_name="registration/logout.html"), name="salir"),
    path('itemView/<int:pk>/', views.itemView, name='itemView'),
    path('cartView/', views.cartView, name='cartView'),
    path('cartConfirm/', views.cartConfirm, name='cartConfirm')
]
