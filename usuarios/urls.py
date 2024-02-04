from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.usuario_view import UsuarioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
