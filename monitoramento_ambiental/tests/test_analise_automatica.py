from django.test import TestCase
from django.urls import reverse
from monitoramento_ambiental.models import AnaliseAutomatica
from monitoramento_ambiental.models import Propriedade

class AnaliseAutomaticaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.propriedade = Propriedade.objects.create(nome="Propriedade Analise", numero_car="CAR12345")
        cls.analise = AnaliseAutomatica.objects.create(
            propriedade=cls.propriedade,
            status="Liberado"
        )

    def test_analise_automatica_status(self):
        self.assertEqual(self.analise.status, "Liberado")

    def test_analise_automatica_propriedade_relation(self):
        self.assertEqual(self.analise.propriedade.nome, "Propriedade Analise")