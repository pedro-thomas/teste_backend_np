from rest_framework import serializers
from ..models.vinculo import Vinculo

class VinculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vinculo
        fields = '__all__'