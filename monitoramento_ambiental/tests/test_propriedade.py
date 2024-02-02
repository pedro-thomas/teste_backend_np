from django.test import TestCase
from monitoramento_ambiental.models import Propriedade

class PropriedadeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Adicionando todos os campos obrigatórios, incluindo 'liberado'
        cls.propriedade = Propriedade.objects.create(
            nomePropriedade="Propriedade Teste",
            numeroCar="CAR123456",
            uf="Estado Teste",
            municipio="Município Teste",
            pais="País Teste",
            liberado=1  # Assumindo que este campo é um inteiro conforme o erro sugere
        )

    def test_propriedade_creation(self):
        self.assertTrue(isinstance(self.propriedade, Propriedade))
        self.assertEqual(self.propriedade.nomePropriedade, "Propriedade Teste")
