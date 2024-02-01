from rest_framework import viewsets
from ..models.vinculo import Vinculo
from ..serializers.vinculo_serializer import VinculoSerializer

class VinculoViewSet(viewsets.ModelViewSet):
    queryset = Vinculo.objects.all()
    serializer_class = VinculoSerializer
