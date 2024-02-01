from rest_framework import viewsets
from ..models.produtor import Produtor
from ..serializers.protudor_serializer import ProdutorSerializer

class ProdutorViewSet(viewsets.ModelViewSet):
    queryset = Produtor.objects.all()
    serializer_class = ProdutorSerializer
