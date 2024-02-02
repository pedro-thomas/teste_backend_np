from rest_framework import serializers
from ..models.vinculo import Vinculo
from ..models.produtor import Produtor
from ..models.propriedade import Propriedade
from ..serializers.produtor_serializer import ProdutorSerializer 
from ..serializers.propriedade_serializer import PropriedadeSerializer 

class VinculoSerializer(serializers.ModelSerializer):
    idPropriedade = PropriedadeSerializer(read_only=True)
    idProdutor = ProdutorSerializer(read_only=True)

    class Meta:
        model = Vinculo
        fields = '__all__'
