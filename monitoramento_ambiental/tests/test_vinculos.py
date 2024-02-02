from django.test import TestCase
from django.urls import reverse
from monitoramento_ambiental.models import Produtor
from monitoramento_ambiental.models import Propriedade
from monitoramento_ambiental.models import Vinculo

class VinculoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Criando instâncias de Propriedade e Produtor para usar no teste de Vinculo
        cls.propriedade = Propriedade.objects.create(nome="Propriedade Vinculo", numero_car="CAR98765")
        cls.produtor = Produtor.objects.create(nome="Produtor Vinculo", cpf="98765432109")
        cls.vinculo = Vinculo.objects.create(propriedade=cls.propriedade, produtor=cls.produtor)

    def test_vinculo_creation(self):
        self.assertTrue(isinstance(self.vinculo, Vinculo))
        self.assertEqual(self.vinculo.__str__(), f'{self.vinculo.propriedade.nome} - {self.vinculo.produtor.nome}')

    def test_propriedade_relation(self):
        self.assertEqual(self.vinculo.propriedade.nome, "Propriedade Vinculo")

    def test_produtor_relation(self):
        self.assertEqual(self.vinculo.produtor.nome, "Produtor Vinculo")
