from rest_framework import serializers
from ..models.propriedade import Propriedade

class PropriedadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propriedade
        fields = '__all__'