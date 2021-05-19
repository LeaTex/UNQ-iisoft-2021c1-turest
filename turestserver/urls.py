from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('portal.urls')),
    path('admin/', admin.site.urls),
    path('panel/', include('administracion.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
