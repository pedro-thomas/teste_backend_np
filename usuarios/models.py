from django.db import models

class Usuario(models.Model):
    idUsuario = models.BigAutoField(primary_key=True)
    nomeUsuario = models.CharField(max_length=100, blank=True, null=True)
    emailUsuario = models.CharField(max_length=100, blank=True, null=True)
    senhaUsuario = models.CharField(max_length=100, blank=True, null=True)
    descricaoCargo = models.CharField(max_length=100, blank=True, null=True)
    industria = models.CharField(max_length=100, blank=True, null=True)

    class Meta: 
        db_table = 'usuarios'