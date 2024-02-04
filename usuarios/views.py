from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render


class UsuarioViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


def login_page(request):
    return render(request, 'login/login.html')
