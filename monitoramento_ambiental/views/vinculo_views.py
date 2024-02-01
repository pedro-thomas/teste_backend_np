from rest_framework import viewsets
from ..models.vinculo import Vinculo
from ..serializers.vinculo_serializer import VinculoSerializer
from rest_framework.permissions import IsAuthenticated

class VinculoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Vinculo.objects.all()
    serializer_class = VinculoSerializer
