from django.db import models
from .produtor import Produtor
from .propriedade import Propriedade

class Vinculo(models.Model):
    idVinculo = models.BigAutoField(primary_key=True)
    idPropriedade = models.ForeignKey(Propriedade, db_column='idPropriedade', on_delete=models.CASCADE)
    idProdutor = models.ForeignKey(Produtor, db_column='idProdutor', on_delete=models.CASCADE)

    class Meta: 
        db_table = 'vinculos'

    def __str__(self):
        nome_propriedade = self.idPropriedade.nomePropriedade if self.idPropriedade and self.idPropriedade.nomePropriedade else 'Propriedade Desconhecida'
        nome_produtor = self.idProdutor.nomeProdutor if self.idProdutor and self.idProdutor.nomeProdutor else 'Produtor Desconhecido'
        return f'{nome_propriedade} - {nome_produtor}'