from rest_framework import generics, status
from ..models.historico_busca import HistoricoBusca
from ..serializers.historico_busca_serializer import HistoricoBuscaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404


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

class HistoricoBuscaListView(ListView):
    model = HistoricoBusca
    template_name = '../templates/historico_busca/listar_historico_busca.html'
    context_object_name = 'historicos'

@login_required
def apagar_historico_busca(request, id):
    historico = get_object_or_404(HistoricoBusca, id=id)
    historico.delete()
    return redirect('listar_historico_busca')