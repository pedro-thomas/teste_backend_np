from django.db import models

class Propriedade(models.Model):
    idPropriedade = models.BigAutoField(primary_key=True)
    nomePropriedade = models.CharField(max_length=100, blank=True, null=True)
    numeroCar = models.CharField(max_length=100, blank=True, null=True)
    uf = models.CharField(max_length=100, blank=True, null=True)
    municipio = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    status = models.BooleanField(default=True)
    liberado = models.IntegerField()

    class Meta: 
        db_table = 'propriedades'