from django.test import TestCase
from monitoramento_ambiental.models import AnaliseAutomatica

class AnaliseAutomaticaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.analise = AnaliseAutomatica.objects.create(
            produtorNome="Nome do Produtor",
            produtorCpf="123.456.789-09",
            propriedadeNome="Propriedade Analise",
            car="CAR12345",
            municipio="Municipio",
            uf="UF",
            estadoMonitoramento=1,  # Supondo que este seja um valor válido para o seu campo
            status=True
        )

    def test_analise_automatica_status(self):
        self.assertTrue(self.analise.status)

    def test_analise_automatica_propriedade_nome(self):
        self.assertEqual(self.analise.propriedadeNome, "Propriedade Analise")
