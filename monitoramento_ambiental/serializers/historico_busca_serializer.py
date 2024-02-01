
from rest_framework import serializers
from ..models.historico_busca import HistoricoBusca

class HistoricoBuscaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoBusca
        fields = '__all__'
