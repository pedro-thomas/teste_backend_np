from rest_framework import generics
from ..models.historico_busca import HistoricoBusca
from ..serializers.historico_busca_serializer import HistoricoBuscaSerializer
from rest_framework.permissions import IsAuthenticated


class HistoricoBuscaList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = HistoricoBusca.objects.all()
    serializer_class = HistoricoBuscaSerializer
