from rest_framework import viewsets
from ..models.produtor import Produtor
from ..serializers.produtor_serializer import ProdutorSerializer
from rest_framework.permissions import IsAuthenticated
from django.views.generic import ListView



class ProdutorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Produtor.objects.all()
    serializer_class = ProdutorSerializer

class ProdutorListView(ListView):
    model = Produtor
    template_name = '../templates/produtores/listar_produtores.html'
    context_object_name = 'produtores'