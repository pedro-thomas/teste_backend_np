from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    ProdutorViewSet, PropriedadeViewSet, 
    AnaliseAutomaticaViewSet, VinculoViewSet, 
    HistoricoBuscaList,
)
from .views.historico_busca_views import HistoricoBuscaDelete

router = DefaultRouter()
router.register(r'produtores', ProdutorViewSet)
router.register(r'propriedades', PropriedadeViewSet, basename='propriedade')
router.register(r'analises_automaticas', AnaliseAutomaticaViewSet)
router.register(r'vinculos', VinculoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('historico/', HistoricoBuscaList.as_view(), name='historico_buscas'),
    path('historico/<int:pk>/delete/', HistoricoBuscaDelete.as_view(), name='historico_buscas_delete'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
