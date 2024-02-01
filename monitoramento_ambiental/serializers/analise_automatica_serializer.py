from rest_framework import serializers
from ..models.analise_automatica import AnaliseAutomatica

class AnaliseAutomaticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnaliseAutomatica
        fields = '__all__'