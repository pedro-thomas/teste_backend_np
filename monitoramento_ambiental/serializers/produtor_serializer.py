from rest_framework import serializers
from ..models.produtor import Produtor

class ProdutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtor
        fields = '__all__'