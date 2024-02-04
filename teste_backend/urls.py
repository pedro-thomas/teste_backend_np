from django.contrib import admin
from django.urls import path, include
from monitoramento_ambiental.views.base_view import base_page
from usuarios.views.login_view import login_page
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from usuarios.views.login_view import logout_view 
from monitoramento_ambiental.views.propriedade_views import listar_propriedades, detalhes_propriedade, editar_propriedade


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/monitoramento/', include('monitoramento_ambiental.urls')),
    path('api/usuarios/', include('usuarios.urls')),
    path('base/', base_page, name='base_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_view, name='logout'),
    path('propriedades/', listar_propriedades, name='listar_propriedades'),
    path('propriedades/<int:id>/', detalhes_propriedade, name='detalhes_propriedade'),
    path('propriedade/editar/<int:pk>/', editar_propriedade, name='editar_propriedade'),

]
