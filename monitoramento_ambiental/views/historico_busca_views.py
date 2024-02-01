from rest_framework import generics
from ..models.historico_busca import HistoricoBusca
from ..serializers.historico_busca_serializer import HistoricoBuscaSerializer

class HistoricoBuscaList(generics.ListAPIView):
    queryset = HistoricoBusca.objects.all()
    serializer_class = HistoricoBuscaSerializer
