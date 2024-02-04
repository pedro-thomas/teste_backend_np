from rest_framework import viewsets
from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializer
from rest_framework.permissions import IsAuthenticated


class UsuarioViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer