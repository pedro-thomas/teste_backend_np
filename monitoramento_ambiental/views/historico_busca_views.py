from rest_framework import generics, status
from ..models.historico_busca import HistoricoBusca
from ..serializers.historico_busca_serializer import HistoricoBuscaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

class HistoricoBuscaList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = HistoricoBusca.objects.all()
    serializer_class = HistoricoBuscaSerializer

class HistoricoBuscaDelete(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return HistoricoBusca.objects.get(pk=pk)
        except HistoricoBusca.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        historico = self.get_object(pk)
        historico.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
