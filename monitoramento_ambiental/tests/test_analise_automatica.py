from django.test import TestCase
from monitoramento_ambiental.models import AnaliseAutomatica

class AnaliseAutomaticaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        AnaliseAutomatica.objects.create(
            produtorNome="Produtor Teste",
            produtorCpf="123.456.789-09",
            propriedadeNome="Propriedade Teste",
            car="CAR123456",
            municipio="Municipio Teste",
            uf="UF",
            estadoMonitoramento=1,
            status=True
        )

    def test_analise_automatica_creation(self):
        analise = AnaliseAutomatica.objects.get(id=1)
        self.assertEqual(analise.produtorNome, "Produtor Teste")
        self.assertEqual(analise.produtorCpf, "123.456.789-09")
        self.assertEqual(analise.propriedadeNome, "Propriedade Teste")
        self.assertEqual(analise.car, "CAR123456")
        self.assertEqual(analise.municipio, "Municipio Teste")
        self.assertEqual(analise.uf, "UF")
        self.assertEqual(analise.estadoMonitoramento, 1)
        self.assertTrue(analise.status)
