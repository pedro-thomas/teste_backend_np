from django.db import models

class Produtor(models.Model):
    idProdutor = models.BigAutoField(primary_key=True)
    registroIndividual = models.CharField(max_length=100, blank=True, null=True)
    nomeProdutor = models.CharField(max_length=100, blank=True, null=True)
    status = models.BooleanField(default=True)

    class Meta: 
        db_table = 'produtores'

    def __str__(self):
        return self.nomeProdutor