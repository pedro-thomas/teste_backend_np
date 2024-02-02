from rest_framework import viewsets
from ..models.produtor import Produtor
from ..serializers.produtor_serializer import ProdutorSerializer
from rest_framework.permissions import IsAuthenticated


class ProdutorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Produtor.objects.all()
    serializer_class = ProdutorSerializer
