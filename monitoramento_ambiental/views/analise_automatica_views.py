from rest_framework import viewsets
from ..models.analise_automatica import AnaliseAutomatica
from ..serializers.analise_automatica_serializer import AnaliseAutomaticaSerializer

class AnaliseAutomaticaViewSet(viewsets.ModelViewSet):
    queryset = AnaliseAutomatica.objects.all()
    serializer_class = AnaliseAutomaticaSerializer
