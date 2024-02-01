from rest_framework import viewsets
from ..models.analise_automatica import AnaliseAutomatica
from ..serializers.analise_automatica_serializer import AnaliseAutomaticaSerializer
from rest_framework.permissions import IsAuthenticated

class AnaliseAutomaticaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AnaliseAutomatica.objects.all()
    serializer_class = AnaliseAutomaticaSerializer
