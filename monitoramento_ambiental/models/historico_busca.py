from django.db import models
from django.utils import timezone

class HistoricoBusca(models.Model):
    termo_busca = models.CharField(max_length=255)
    data_hora_busca = models.DateTimeField(default=timezone.now)
    resultado_busca = models.JSONField()

    def __str__(self):
        return self.termo_busca