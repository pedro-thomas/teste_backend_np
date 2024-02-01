from django.db import models
from .produtor import Produtor
from .propriedade import Propriedade

class Vinculo(models.Model):
    idVinculo = models.BigAutoField(primary_key=True)
    idPropriedade = models.ForeignKey(Propriedade, db_column='idPropriedade', on_delete=models.CASCADE)
    idProdutor = models.ForeignKey(Produtor, db_column='idProdutor', on_delete=models.CASCADE)

    class Meta: 
        db_table = 'vinculos'