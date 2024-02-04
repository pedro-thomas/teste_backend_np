from django.contrib import admin
from django.urls import path, include
from monitoramento_ambiental.views.base_view import base_page
from usuarios.views import login_page
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/monitoramento/', include('monitoramento_ambiental.urls')),
    path('api/usuarios/', include('usuarios.urls')),
    path('base/', base_page, name='base_page'),
    path('login/', login_page, name='login_page'),
]
