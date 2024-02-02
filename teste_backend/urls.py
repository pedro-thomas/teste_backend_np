from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/monitoramento/', include('monitoramento_ambiental.urls')),
    path('api/usuarios/', include('usuarios.urls')),
]
