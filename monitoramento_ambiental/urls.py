from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (ProdutorViewSet, PropriedadeViewSet, 
                    AnaliseAutomaticaViewSet, VinculoViewSet, HistoricoBuscaList)

router = DefaultRouter()
router.register(r'produtores', ProdutorViewSet)
router.register(r'propriedades', PropriedadeViewSet, basename='propriedade')
router.register(r'analises_automaticas', AnaliseAutomaticaViewSet)
router.register(r'vinculos', VinculoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('historico_buscas/', HistoricoBuscaList.as_view(), name='historico_buscas'),
]