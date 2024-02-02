from django.test import TestCase
from monitoramento_ambiental.models import Propriedade, Produtor, Vinculo

class VinculoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.propriedade = Propriedade.objects.create(nomePropriedade="Propriedade Vinculo", numeroCar="CAR98765", liberado=1)
        cls.produtor = Produtor.objects.create(nomeProdutor="Produtor Vinculo", registroIndividual="98765432109")
        cls.vinculo = Vinculo.objects.create(idPropriedade=cls.propriedade, idProdutor=cls.produtor)

    def test_vinculo_creation(self):
        self.assertTrue(isinstance(self.vinculo, Vinculo))
        self.assertEqual(f'{self.vinculo.idPropriedade.nomePropriedade} - {self.vinculo.idProdutor.nomeProdutor}', "Propriedade Vinculo - Produtor Vinculo")
