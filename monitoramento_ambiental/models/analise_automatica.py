from django.db import models

class AnaliseAutomatica(models.Model):
    produtorNome = models.CharField(max_length=100, blank=True, null=True)
    produtorCpf = models.CharField(max_length=15, blank=True, null=True)
    propriedadeNome = models.CharField(max_length=100, blank=True, null=True)
    car = models.CharField(max_length=100, blank=True, null=True)
    municipio = models.CharField(max_length=100, blank=True, null=True)
    uf = models.CharField(max_length=100, blank=True, null=True)
    estadoMonitoramento = models.IntegerField(blank=True, null=True)
    status = models.BooleanField(default=True)

    class Meta: 
        db_table = 'analiseAutomatica'