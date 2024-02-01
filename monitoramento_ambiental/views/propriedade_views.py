from rest_framework import viewsets
from ..models.propriedade import Propriedade
from ..models.historico_busca import HistoricoBusca  # Importe o modelo de histórico de buscas
from ..serializers.propriedade_serializer import PropriedadeSerializer
from ..serializers.historico_busca_serializer import HistoricoBuscaSerializer  # Importe o serializer do histórico de buscas
from django.utils import timezone

class PropriedadeViewSet(viewsets.ModelViewSet):
    serializer_class = PropriedadeSerializer

    def get_queryset(self):
        numero_car = self.request.query_params.get('numero_car', None)
        if numero_car is not None:
            queryset = Propriedade.objects.filter(numeroCar=numero_car)

            HistoricoBusca.objects.create(
                termo_busca=numero_car,
                data_hora_busca=timezone.now(),
                resultado_busca=self.serialize_queryset(queryset)
            )
            return queryset

        return Propriedade.objects.all()

    def serialize_queryset(self, queryset):
        serializer = PropriedadeSerializer(queryset, many=True)
        return serializer.data
