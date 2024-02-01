from rest_framework import viewsets
from ..models.propriedade import Propriedade
from ..serializers.propriedade_serializer import PropriedadeSerializer

class PropriedadeViewSet(viewsets.ModelViewSet):
    queryset = Propriedade.objects.all()
    serializer_class = PropriedadeSerializer
