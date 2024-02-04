from django.contrib import admin
from django.urls import path, include
from monitoramento_ambiental.views.base_view import base_page
from usuarios.views.login_view import login_page
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from usuarios.views.login_view import logout_view 
from monitoramento_ambiental.views.propriedade_views import listar_propriedades, detalhes_propriedade, editar_propriedade
from monitoramento_ambiental.views.produtor_views import ProdutorListView
from monitoramento_ambiental.views.historico_busca_views import HistoricoBuscaListView
from monitoramento_ambiental.views.historico_busca_views import apagar_historico_busca
from monitoramento_ambiental.views.propriedade_views import buscar_por_sicar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/monitoramento/', include('monitoramento_ambiental.urls')),
    path('api/usuarios/', include('usuarios.urls')),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_view, name='logout'),
    path('', listar_propriedades, name='listar_propriedades'),
    path('propriedades/<int:id>/', detalhes_propriedade, name='detalhes_propriedade'),
    path('propriedade/editar/<int:pk>/', editar_propriedade, name='editar_propriedade'),
    path('produtores/', ProdutorListView.as_view(), name='listar_produtores'),
    path('historico-busca/', HistoricoBuscaListView.as_view(), name='listar_historico_busca'),
    path('historico-busca/apagar/<int:id>/', apagar_historico_busca, name='apagar_historico_busca'),
    path('buscar-por-sicar/', buscar_por_sicar, name='buscar_por_sicar'),

]
